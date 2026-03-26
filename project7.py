# datetime_utils.py
import datetime
import time

def show_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def date_difference(date1, date2):
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def format_date(date, format_str="%d-%m-%Y"):
    return date.strftime(format_str)

def stopwatch(seconds=5):
    print("Stopwatch started...")
    time.sleep(seconds)
    print("Stopwatch ended!")

def countdown(seconds=5):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time’s up!")


# math_utils.py
import math

def basic_operations(a, b):
    return {"sum": a+b, "diff": a-b, "product": a*b, "division": a/b}

def advanced_operations(x):
    return {"sin": math.sin(x), "cos": math.cos(x), "log": math.log(x), "factorial": math.factorial(int(x))}

def compound_interest(principal, rate, time):
    return principal * ((1 + rate/100) ** time)

def area_circle(radius):
    return math.pi * radius**2


# random_utils.py
import random

def random_number(start=1, end=100):
    return random.randint(start, end)

def random_list(size=5):
    return [random.randint(1, 100) for _ in range(size)]

def random_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    return "".join(random.choice(chars) for _ in range(length))

def random_sampling(dataset, k=3):
    return random.sample(dataset, k)

def random_otp():
    return random.randint(100000, 999999)


# uuid_utils.py
import uuid

def generate_uuid():
    return str(uuid.uuid4())


# file_utils.py
def save_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")
    return "Data saved successfully!"


# mypackage/conversions.py
def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


# mypackage/advanced_math.py
def square(n):
    return n**2

def cube(n):
    return n**3


# main.py

def main():
    while True:
        print("\n--- Multi-Utility Toolkit ---")
        print("1. Show Current Date & Time")
        print("2. Date Difference")
        print("3. Math Operations")
        print("4. Generate Random Password")
        print("5. Generate UUID")
        print("6. Save Data to File")
        print("7. Unit Conversions")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(show_current_datetime())
        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            print("Difference:", date_difference(d1, d2), "days")
        elif choice == "3":
            a, b = 10, 5
            print(basic_operations(a, b))
        elif choice == "4":
            print("Password:", random_password())
        elif choice == "5":
            print("UUID:", generate_uuid())
        elif choice == "6":
            data = input("Enter data to save: ")
            print(save_to_file("output.txt", data))
        elif choice == "7":
            print("10 km =", km_to_miles(10), "miles")
            print("100°C =", celsius_to_fahrenheit(100), "°F")
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()