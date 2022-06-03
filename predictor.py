import datetime

time_now = datetime.datetime.now()
time_str = time_now.strftime("%A, %d/%m/%Y %H:%M")

RESTRICTION_START1 = datetime.time(6, 0, 0)
RESTRICTION_END1 = datetime.time(9, 30, 0)
RESTRICTION_START2 = datetime.time(16, 0, 0)
RESTRICTION_END2 = datetime.time(21, 0, 0)

DAY_CORRESPONDING_PLATES = {"Monday": [1, 2], "Tuesday": [
    3, 4], "Wednesday": [5, 6], "Thursday": [7, 8], "Friday": [9, 0]}

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

license_plate = ""
license_plate_last_digit = 0


def is_restricted_day_plate(day, plates):
    """Returns True if the plate number has restriction on the corresponding weekday
    """
    for i in DAY_CORRESPONDING_PLATES:
        if i == day:
            plates_day = DAY_CORRESPONDING_PLATES.get(i)
        else:
            plates_day = ""
            # print(DAY_CORRESPONDING_PLATES.get(i))
    if plates in plates_day:
        # print("You have restriction.")
        return True
    else:
        return False


def asdf(day, plate_number):
    if day in DAY_CORRESPONDING_PLATES:
        if plate_number in DAY_CORRESPONDING_PLATES.items():
            return True


def is_applicable_plate_day(day):
    # for day in DAY_CORRESPONDING_PLATES:
    #     print(day)
    if day in DAY_CORRESPONDING_PLATES:
        return True
    else:
        return False


def is_applicable_day(day):
    """ Returns True if day is weekday
    """
    if day in WEEKDAYS:
        return True
    else:
        return False


def time_in_range(start, end, sel_time):
    """Returns whether current is in the range [start, end]
        True if is within range -> restricted for driving
        False if is not within range -> not restricted for driving
    """
    return start <= sel_time <= end


def input_time():
    """Receives a string input for time to calculate,
        and returns it in time object
    """
    print("\nPlease enter the time to check restriction:")
    print("Time format is hh:mm")
    input_time_str = input()
    input_time = datetime.datetime.strptime(input_time_str, "%H:%M").time()
    return input_time


def get_week_day(date):
    """Given a date in string format dd/mm/yyyy,
        returns corresponding day of the week in string type
    """
    selected_date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%A")
    return selected_date


def input_date():
    print("\nPlease enter the date to check restriction:")
    print("Date format is dd/mm/yyyy")
    input_date = input()
    return input_date


def get_last_digit_lp(license_plate):
    spl = []
    spl[:] = license_plate
    return spl[-1]


def input_license_plate():
    print("Please enter your car license plate:")
    license_plate = input()
    return license_plate


def welcome_message():
    print("Welcome to Pico y Placa Predictor")
    print("This program will help you know if your car is allowed to be used during \"Pico y Placa\" restriction in Quito-Ecuador.")
    print("Note: All format dates must be dd/mm/yyyy and hours will use 24h format")
    print(f"\n\nToday is {time_str}")


def run():
    # welcome_message()
    # license_plate = input_license_plate()
    # print(f"\nYour license plate number is {license_plate}")
    # license_plate_last_digit = get_last_digit_lp(license_plate)
    # print(f"which last digit number is {license_plate_last_digit}")
    # sel_date = input_date()
    # sel_day = get_week_day(sel_date)
    # print(f"The selected date is {sel_date} and the day of the week is {sel_day}")
    # sel_time = input_time()
    # print(f"The selected time is {sel_time}")

    # print(is_applicable_day(sel_day))

    # print(is_applicable_plate_day("Mondays"))

    # print(asdf("Monday", 2))

    print(is_restricted_day_plate("Tuesday", 3))


if __name__ == '__main__':
    run()
