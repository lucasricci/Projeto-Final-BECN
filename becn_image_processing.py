from PIL import Image
import numpy as np

names = [
    {"Nome": "Agata", "Grau": "2"},
    {"Nome": "Amanda", "Grau": "1"},
    {"Nome": "Ana Banana", "Grau": "4"},
    {"Nome": "Betania", "Grau": "1"},
    {"Nome": "Josefa", "Grau": "2"},
    {"Nome": "Lauriane II", "Grau": "1"},
    {"Nome": "Luisa Sonza", "Grau": "2"},
    {"Nome": "Mariana", "Grau": "3"},
    {"Nome": "Otavia", "Grau": "1"},
    {"Nome": "Sam", "Grau": "2"},
    {"Nome": "Tereza", "Grau": "4"},
]

for c in range(len(names)):
    file = open("results.csv", "a")
    im = Image.open(f"C:\\Users\\lucas\\Desktop\\BECN\\{names[c]["Nome"]}.jpg")

    px = im.load()
    pixel_matrix = []

    for x in range(im.width):
        for y in range(im.height):
            pixel = im.getpixel((x, y))
            pixel_matrix.append(pixel)

    r = np.mean(np.array(pixel_matrix)[:, 0])
    g = np.mean(np.array(pixel_matrix)[:, 1])
    b = np.mean(np.array(pixel_matrix)[:, 2])

    #print('#%02x%02x%02x' % (int(r), int(g), int(b)))
    output = f"{names[c]["Nome"]}, {r:.0f}, {g:.0f}, {b:.0f}\n"
    file.write(output)
    file.close()
