"""
Demonstration of scope

"""

# global constant
DAYS_OF_THE_WEEK = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]

# global variable - avoid
g_name = "Charlie Brown"


def main():
    for day in DAYS_OF_THE_WEEK:
        print(day)

    global g_name
    g_name = "Lucy"

    print(f"In Main {g_name}")
    greeting()


def greeting():
    print(f"Hello {g_name}")
    # print(d)


main()
