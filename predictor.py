import datetime

time_now = datetime.datetime.now()
time_str = time_now.strftime("%A, %d/%m/%Y %H:%M")

RESTRICTION_START1 = datetime.time(6, 0, 0)
RESTRICTION_END1 = datetime.time(9, 30, 0)
RESTRICTION_START2 = datetime.time(16, 0, 0)
RESTRICTION_END2 = datetime.time(21, 0, 0)

DAY_CORRESPONDING_PLATES = {"Monday": [1, 2], "Tuesday": [
    3, 4], "Wednesday": [5, 6], "Thursday": [7, 8], "Friday": [9, 0]}


def prediction(applicable_day_plate, applicable_hours):
    if (applicable_day_plate and applicable_hours):
        print("You can't drive.")
    else:
        print("You can drive.")
        if applicable_day_plate:
            st1 = RESTRICTION_START1.strftime("%H:%M")
            st2 = RESTRICTION_START2.strftime("%H:%M")
            end1 = RESTRICTION_END1.strftime("%H:%M")
            end2 = RESTRICTION_END2.strftime("%H:%M")
            print("\nRemember that \"Pico y Placa\" restriction hours are:")
            print(
                f"From {st1} to {end1}, and from {st2} to {end2}.")


def is_applicable_hour(sel_time):
    if time_in_range(RESTRICTION_START1, RESTRICTION_END1, sel_time) or time_in_range(RESTRICTION_START2, RESTRICTION_END2, sel_time):
        return True
    else:
        return False


def is_applicable_day_plate(weekday, plate_last_digit):
    if is_applicable_day(weekday) and plate_last_digit in DAY_CORRESPONDING_PLATES[weekday]:
        print(
            f"\nYour license plate number has restriction on {weekday}s!\nPlease check hours for applicability.")
        return True
    else:
        print(
            f"\nYour license plate number doesn't have restriction on {weekday}s!. You can drive all day.")
        exit()


def is_applicable_day(day):
    if day in DAY_CORRESPONDING_PLATES:
        return True
    else:
        return False


def time_in_range(start, end, sel_time):
    """Returns whether selected time is in the range of [start, end]
        True if is within range -> restricted for driving
        False if is not within range -> not restricted for driving
    """
    if start <= sel_time <= end:
        return True
    else:
        return False


def input_time():
    """Receives a string input for time to calculate,
        and returns it in datetime object
    """
    print("\nEnter the time [hh:mm] to check restriction:")
    input_time_str = input()
    print(f"The selected time is {input_time_str}")
    input_time = datetime.datetime.strptime(input_time_str, "%H:%M").time()
    return input_time


def get_week_day(date):
    """Given a date in string format dd/mm/yyyy,
        returns corresponding day of the week in string type
        if the day is weekend, program will end.
    """
    selected_date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%A")
    print(f"and the day of the week is {selected_date}")
    if is_applicable_day(selected_date):
        return selected_date
    else:
        print(
            f"\nYou can be on the road, since {selected_date} has no restrction.")
        exit()


def input_date():
    print("\nPlease enter the date [dd/mm/yyyy] to check restriction:")
    input_date = input()
    print(f"The selected date is {input_date}")
    return input_date


def get_last_digit_lp(license_plate):
    return int(license_plate[-1])


def input_license_plate():
    print("Please enter your car license plate:")
    license_plate = input()
    return license_plate


def welcome_message():
    print("Welcome to Pico y Placa Predictor")
    print("This program will help you know if your car is allowed to be used during \"Pico y Placa\" restriction in Quito-Ecuador.")
    print("Please remember that holidays don't apply ")
    print("Note: All format dates must be dd/mm/yyyy and hours will use 24h format")
    print(f"\n\nToday is {time_str}")


def run():
    welcome_message()

    license_plate = input_license_plate()
    print(f"\nYour license plate number is {license_plate}")

    license_plate_last_digit = get_last_digit_lp(license_plate)
    print(f"which last digit number is {license_plate_last_digit}")

    sel_date = input_date()
    sel_day = get_week_day(sel_date)

    applicable_day_plate = is_applicable_day_plate(
        sel_day, license_plate_last_digit)

    sel_time = input_time()

    applicable_time = is_applicable_hour(sel_time)
    prediction(applicable_day_plate, applicable_time)


if __name__ == '__main__':
    run()
