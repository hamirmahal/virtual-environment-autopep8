import datetime


def print_with_time(info: str):
    # Get the current time in HH:MM:SS format
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] {info}")


print_with_time("Hello.")
