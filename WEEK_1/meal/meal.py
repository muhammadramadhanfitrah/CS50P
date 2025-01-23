def main():
    time_input = input("What time is it? ")

    meal_time(time_input)


def convert(time):
    hours, minutes = time.split(":")
    total_hours = int(hours) + int(minutes) / 60
    return total_hours


def meal_time(times):
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    time_hours = convert(times)

    if breakfast_start <= time_hours <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= time_hours <= lunch_end:
        print("lunch time")
    elif dinner_start <= time_hours <= dinner_end:
        print("dinner time")


if __name__ == "__main__":
    main()
