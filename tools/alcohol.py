#!/bin/python3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from sys import argv
from tkinter import Button, Label, StringVar, Tk
from uuid import uuid4

DATA_DIR = Path(__file__).parent / ".py-data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def now():
    return datetime.now(timezone.utc)


class DataFile:
    data_filepath: Path
    units: list[datetime]
    safe: datetime | None
    countdown: str

    def __init__(self, file_suffix: str | None = None) -> None:
        self.data_filepath = (
            DATA_DIR / f"alcohol{f'_{file_suffix}' if file_suffix else ''}.py-data"
        ).resolve()
        self.load()
        self.test()

    def save(self):
        self.test()
        with open(self.data_filepath, "w") as data:
            data.write("\n".join(f"{dt.timestamp()}" for dt in self.units))

    def load(self):
        self.units = []
        try:
            with open(self.data_filepath, "r") as data:
                for line in data:
                    try:
                        self.units.append(datetime.fromtimestamp(float(line), tz=timezone.utc))
                    except ValueError:
                        pass
        except FileNotFoundError:
            pass

    def test(self):
        self.safe = None
        unit_count = 0
        for unit in self.units:
            if self.safe is None or (self.safe < unit):
                self.safe = unit + timedelta(hours=1)
                unit_count = 1
            else:
                self.safe += timedelta(hours=1)
                unit_count += 1
        if self.safe is None:
            self.countdown = "00:00:00"
            return
        keep_before = self.safe - timedelta(hours=unit_count, minutes=1)
        self.units = [unit for unit in self.units if unit >= keep_before]
        if self.safe < now():
            self.countdown = "00:00:00"
            return
        countdown = self.safe - now()
        if countdown.days:
            self.countdown = f"{countdown.days} Day(s)"
            return
        hours, remainder = divmod(countdown.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.countdown = f"{hours:02}:{minutes:02}:{seconds:02}"

    def plus_one(self):
        self.units.append(now())
        self.save()


if __name__ == "__main__":
    data = DataFile((argv[1] if len(argv) >= 2 else input("Name: ") or str(uuid4())).lower())
    kill_flag = False

    def kill():
        global kill_flag
        kill_flag = True

    root = Tk()
    root.title("Alcohol Counter")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)
    safe_text = StringVar()
    Label(root, textvariable=safe_text, font=("", 32)).grid(row=0, column=0, sticky="NSEW")
    countdown_text = StringVar()
    Label(root, textvariable=countdown_text, font=("", 128)).grid(row=1, column=0, sticky="NSEW")
    Button(root, text="Drink 1 Unit", command=data.plus_one, font=("", 64)).grid(
        row=2, column=0, sticky="NSEW"
    )
    Button(root, text="Close", command=kill, font=("", 64)).grid(row=3, column=0, sticky="NSEW")
    Label(root, text=str(data.data_filepath), font=("", 8)).grid(row=4, column=0, sticky="NSEW")
    root.protocol("WM_DELETE_WINDOW", kill)
    while not kill_flag:
        try:
            data.test()
            safe_text.set(data.safe.strftime("%Y-%m-%d %H:%M:%S") if data.safe is not None else "")
            countdown_text.set(data.countdown)
            root.update()
        except KeyboardInterrupt:
            kill()
    root.destroy()
