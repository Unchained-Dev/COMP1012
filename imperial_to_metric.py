feet = int(input("input feet value: "));
inches = int(input("input inches value: "));

def convert(inches, feet):
    cm = 0;
    tempInches = inches * 2.54;
    tempFeet = feet * 30.48;

    cm = tempFeet + tempInches;

    return cm;

cm = convert(inches, feet);

print(f'{feet} feet, {inches} inch = {cm:.2f} cm');
