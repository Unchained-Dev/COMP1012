import sys

# Dictionary that defines the capacity of each container type
containers = {
    'small': 1,
    'medium': 5,
    'large': 20,
    'huge': 50
}

# Function to sort widgets into containers
def sort(widgets):
    temp = widgets  # Create a temporary variable to store the remaining widgets
    sortedWidgets = {
        'small': 0,
        'medium': 0,
        'large': 0,
        'huge': 0
    }  # Initialize a dictionary to store the count of each container type

    while temp > 0:
        if (temp / containers['huge'] >= 1):  # Check if there are enough widgets for a huge container
            sortedWidgets['huge'] += 1  # Increment the count of huge containers
            temp -= containers['huge']  # Subtract the capacity of a huge container from temp
        elif (temp / containers['large'] >= 1):  # Check if there are enough widgets for a large container
            sortedWidgets['large'] += 1  # Increment the count of large containers
            temp -= containers['large']  # Subtract the capacity of a large container from temp
        elif (temp / containers['medium'] >= 1):  # Check if there are enough widgets for a medium container
            sortedWidgets['medium'] += 1  # Increment the count of medium containers
            temp -= containers['medium']  # Subtract the capacity of a medium container from temp
        elif (temp / containers['small'] >= 1):  # Check if there are enough widgets for a small container
            sortedWidgets['small'] += 1  # Increment the count of small containers
            temp -= containers['small']  # Subtract the capacity of a small container from temp

    return sortedWidgets

print("input a non-integer to end the program\n")

while True:
    try:
        widgets = input("provide the amount of widgets: ")
    except EOFError:
        print("\nYou have exited the program\n")
        sys.exit()

    try:
        widgets = int(widgets)
    except ValueError:
        print("\nYou have exited the program\n")
        break

    sortedWidgets = sort(widgets)

    print("There are ", end="")

    for key in sortedWidgets.keys():
        if (sortedWidgets[key] == 1):
            print(f'{sortedWidgets[key]} {key} box ', end="")
        else:
            print(f'{sortedWidgets[key]} {key} boxes ', end="")

    print("\n")

