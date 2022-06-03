import datetime

time_now = datetime.datetime.now()
time_str = time_now.strftime("%A, %d/%m/%Y %H:%M")

start = datetime.time(6, 0, 0)
end = datetime.time(9, 30, 0)
# current = datetime.datetime.now().time()
# print(time_in_range(start, end, current))


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
        returns corresponding weekday in string type
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
    welcome_message()
    license_plate = input_license_plate()
    print(f"\nYour license plate number is {license_plate}")
    license_plate_last_digit = get_last_digit_lp(license_plate)
    print(f"which last digit number is {license_plate_last_digit}")
    sel_date = input_date()
    sel_weekday = get_week_day(sel_date)
    print(f"The selected date is {sel_date} and its weekday is {sel_weekday}")
    sel_time = input_time()
    print(f"The selected time is {sel_time}")


if __name__ == '__main__':
    run()
