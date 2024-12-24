from os import environ, getcwd, name, uname
from sys import argv
from random import choice


GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
RESET = "\033[0m"
RUDE_MSGS = (
    "No. I don't like you",
    "Piss Off",
    "Leave me alone",
    "Go Away",
)
for _ in range(int(argv[1]) if len(argv) > 1 else 10):
    try:
        input(
            f"{getcwd()}> "
            if name == "nt"
            else f"{GREEN}{environ['USER']}@{uname().nodename}:{BLUE}{environ['PWD'].replace(environ['HOME'], '~')}{RESET}$ "
        )
        print(choice(RUDE_MSGS))
    except KeyboardInterrupt:
        print("\nYou can't escape that easily.")
