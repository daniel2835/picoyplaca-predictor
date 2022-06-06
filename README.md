# Pico y Placa Predictor

### This is Pico Y Placa Predictor version 2.0

The improvements are:

- An improved user-friendly interface. It will remind you of the restriction hours in case your car has restriction on selected date but you selected a non-applicable hour.
- Direct output result. You don't need to go through all the input process if it is detected that the selected day is weekend or if your car's license plate number doesn't have restriction on selected day.

This Python application will help you know if your car's license plate number is available to be on the road in Quito-Ecuador, according to the applicable laws of "Pico y Placa"

> Please always remember to check updated conditions of Pico y Placa.

As of May 2022, restriction applies for two digit plate numbers per day:

| Day       | Plate numbers |
| --------- | ------------- |
| Monday    | 1 and 2       |
| Tuesday   | 3 and 4       |
| Wednesday | 5 and 6       |
| Thursday  | 7 and 8       |
| Friday    | 9 and 0       |
| Saturday  | N/A           |
| Sunday    | N/A           |

Restriction hours start from 06:00 to 09:30 and from 16:00 to 21:00.

## Requirements

You must have Python installed in order to run this application.

This application was developed in Python 3.10.0 but no special libraries were used apart from "datetime" library.

It is recommended to run it on console.

## User guide

This application is user-friendly and will guide you (with texts on console) through all the process. You must enter the required information via keyboard input.

> Note that as explained above, you don't need to go through the whole input process if it is detected that restriction is not applicable. Result will be shown as soon as possible, terminating the program excecution.

1. Run predictor.py on console.
2. The app will show you at all times what the corresponding input format is.
3. First, you'll be asked to enter your full car license plate number.
4. You should see on console the plate number you entered and its last digit.
5. Now you will have to enter the date for calculation.
6. On console, it's shown the date you have selected and its corresponding day of the week. Furthermore, it could show a warning message if your license plate number has restriction on selected date.
7. The last input you must enter is the time to check if restriction applies.
8. Finally, a text will show you if your car can be on the road or not.

### Thank you for using Pico Y Placa Predictor!
