import datetime
# import calendar

# curr_date = datetime.datetime.today()
time_now = datetime.datetime.now()
time_str = time_now.strftime("%A, %d/%m/%Y %H:%M")


def getLastDigitLP(licensePlate):
    spl = []
    spl[:] = licensePlate
    return spl[-1]


def inputLicensePlate():
    print("Please enter your car license plate")
    licensePlate = input()
    return licensePlate


def welcomeMessage():
    print("Welcome to Pico y Placa Predictor")
    print("This program will help you know if your car is allowed to be used during \"Pico y Placa\" restriction in Quito-Ecuador.")
    print("Note: All dates format will be dd/mm/yyyy and hours will be 24h format")
    print(f"\n\nToday is {time_str}")


def run():
    welcomeMessage()
    licensePlate = inputLicensePlate()
    # print test for licensePlate:
    print(f"License {licensePlate}")
    licensePlateLastDigit = getLastDigitLP(licensePlate)
    # print test for lastdigit
    print(licensePlateLastDigit)


if __name__ == '__main__':
    run()
