"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    semester_cost_per_credit = annual_cost / SEMESTERS_PER_YEAR / credits
    cs1430_semester_cost = semester_cost_per_credit * CS1430_CREDITS
    return cs1430_semester_cost / CS1430_MEETINGS_PER_SEMESTER


def non_computer_science_credits(credits):
    return credits - CS1430_CREDITS


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = input("Enter the total cost for one year: ")
    annual_cost = float(annual_cost)


    credits = input("Enter the number of credits for this semester: ")
    credits = float(credits)


    while True:
        # Show your menu here.
        print("Menu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class meeting")
        print("6. Non-CS 1430 credits")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per CS 1430 class meeting: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            print(f"Non-CS 1430 credits: {non_computer_science_credits(credits)}")
        else:
            print("Invalid, please choose another option.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
