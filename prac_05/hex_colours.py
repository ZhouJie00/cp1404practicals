COLOR_NAMES = {"Turquoise": "#40E0D0", "Coral": "#FF7F50",
              "Royalblue": "#4169E1", "Lavender": "#E6E6FA",
              "Gold": "#FFD700", "Teal": "#008080",
              "Salmon": "#FA8072", "Orchid": "#DA70D6",
              "Slategray": "#708090", "Firebrick": "#B22222"}



print(COLOR_NAMES)
selected_option = input("Enter a color name (e.g. Red): ").title()
while selected_option != "":
    print("The code for \"{}\" is {}".format(selected_option, COLOR_NAMES.get(selected_option)))
    choice = input("Enter a color name: ").title()

print("Thank you")
