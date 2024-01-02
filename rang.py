import math
def f(input, standard_colors):
    min=float('inf')
    ncolor = None
    for name, standard in standard_colors.items():
        distance = d(input, standard)
        if distance < min:
            min = distance
            ncolor = name
    return ncolor
def d(color1, color2):
    return math.sqrt((color1["R"] - color2["R"])**2 + (color1["G"] - color2["G"])**2 + (color1["B"] - color2["B"])**2)
colors = {
    "Light salmon": {"R": 255, "G": 160, "B": 122},
    "Salmon": {"R": 250, "G": 128, "B": 114},
    "darksalmon": {"R": 233, "G": 150, "B": 122},
    "Lightcorul": {"R": 240, "G": 128, "B": 128},
    "indianred": {"R": 205, "G": 92, "B": 92},
    "red": {"R": 255, "G": 0, "B": 0}
}
input = {
    "R": int(input("Enter the value for R (0-255): ")),
    "G": int(input("Enter the value for G (0-255): ")),
    "B": int(input("Enter the value for B (0-255): "))
}
ncolor = f(input, colors)
if ncolor is not None:
    print(ncolor)
else:
    print("None")
