def total_gifts(days_of_christmas: int = 12, /, verbose: bool = False) -> int:
    day_of_christmas = 1
    total_gifts = 0
    while day_of_christmas <= days_of_christmas:
        new_gifts = tuple(range(day_of_christmas, 0, -1))
        total_gifts += sum(new_gifts)
        if verbose:
            print(
                f"On the {day_of_christmas} st/nd/th day of christmas my true love gave to me {new_gifts} new gifts bringing me to {total_gifts} total gifts."
            )
        day_of_christmas += 1
    return total_gifts


if __name__ == "__main__":
    total_gifts(12, verbose=True)
