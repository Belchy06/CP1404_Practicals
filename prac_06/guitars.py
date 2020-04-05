"""
CP1404 Practical - Programming language do-from-scratch exercise
"""

from prac_06.Guitar import Guitar


def main():
    guitars = []

    # Test code
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = validate_numeric_input("Year")
        cost = validate_numeric_input("Cost")
        guitars.append(Guitar(name, year, cost))

    print_guitars(guitars)


def validate_numeric_input(input_name):
    """
    Both the year and cost need to be above 0 to be valid numeric inputs
    """
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input("{}}: ".format(input_name)))
            if user_input < 0:
                print("{} must be greater than or equal to 0".format(input_name))
            else:
                valid_input = True
        except:
            print("Please enter a valid {}!".format(input_name))
    return user_input


def print_guitars(guitar_list):
    """
    Enumerate over the guitar_list and print the required information with the correct formatting
    """
    for index, guitar in enumerate(guitar_list, 1):
        print("Guitar {}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {}"
              .format(index,
                      "(vintage)" if guitar.is_vintage() else "",
                      guitar=guitar))


main()
