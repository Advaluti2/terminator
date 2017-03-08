import random

filename = ""
x = 0
alpha = ["a", "i", "o", "e", "u", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "w", "v", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", " ", "A", "I", "O", "E", "U", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "W", "V", "X", "Y", "Z"]
beta = [".csv", ".txt", ".png", ".psd", ".lsd", ".pdo", ".json", ".docx", ".pdf"]
while True:
    while x <= 26:
        filename += random.choice(alpha)
        x +=1
    name = filename + random.choice(beta)
    filename = ""
    x = 0
    file = open(name, "w")
    file.write("")
    file.close()
