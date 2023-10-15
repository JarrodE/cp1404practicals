"""
CP1404/CP5632 Practical
Program that allows you to look up hexadecimal colour codes
"""

COLOURS = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff", "aqua": "#00ffff",
           "babyblue": "#89cff0", "beige": "#f5f5dc", "black": "#000000", "bone": "#e3dac9", "camel": "#c19a6b",
           "dandelion": "#f0e130"}
print(COLOURS)

for code, name in COLOURS.items():
    print(f"{code:13} is: {name}")

colour = input("Enter colour: ").lower()

while colour != "":
    try:
        print(colour, "is:", COLOURS[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
