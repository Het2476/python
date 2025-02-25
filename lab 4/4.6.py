def hours():
    for hour in range(24):
        if hour == 0:
            print("12 Midnight")
        elif hour < 12:
            print(f"{hour} AM")
        elif hour == 12:
            print("12 Noon")
        else:
            print(f"{hour - 12} PM")
hours()