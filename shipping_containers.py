import sys

containers = {
    'small': 1,
    'medium': 5,
    'large': 20,
    'huge': 50
}

def sort(widgets):
    temp = widgets;
    sortedWidgets = {
        'small': 0,
        'medium': 0,
        'large': 0,
        'huge': 0
    }

    while temp > 0:
        if (temp / containers['huge']  >= 1):
            sortedWidgets['huge'] += 1;
            temp -= containers['huge'];
        elif (temp / containers['large'] >= 1):
            sortedWidgets['large'] += 1;
            temp -= containers['large'];
        elif (temp / containers['medium'] >= 1):
            sortedWidgets['medium'] += 1;
            temp -= containers['medium'];
        elif (temp / containers['small'] >= 1):
            sortedWidgets['small'] += 1;
            temp -= containers['small'];

    return sortedWidgets;

print("input a non integer to end program\n");

while True:
    try:
        widgets = input("provide the amount of widgets: ");

    except EOFError:
        print("\nYou have exited the program\n");
        sys.exit();
    
    try:
        widgets = int(widgets);
    
    except ValueError:
        print("\nYou have exited the program\n");
        break;
    
    sortedWidgets = sort(widgets);
    
    print("There are ", end="");

    for key in sortedWidgets.keys():
        if (sortedWidgets[key] == 1):
            print(f'{sortedWidgets[key]} {key} box ', end="");
        else:
            print(f'{sortedWidgets[key]} {key} boxes ', end="");

    print("\n");
