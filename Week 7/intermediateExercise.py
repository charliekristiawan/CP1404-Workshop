color_name = {"Lavender": "#e6e6fa", "Beige": "#f5f5dc", "Darkviolet": "#00ced1", "Greenyellow": "#adff2f", "Blanchedalmond": "#ffebcd", "Coral": "#ff7f50", "Dimgray": "#696969", "Limegreen": "#32cd32", "Lightblue": "#add8e6", "Cadetblue": "#5f9ea0"}
name = input("Enter a name: ").capitalize()

for key,value in color_name.items():
    if name == key:
        print(value)
if name not in color_name.keys():
    print("Invalid input, try again")