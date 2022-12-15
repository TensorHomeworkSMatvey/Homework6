def enc_XOR(text, key):
    return "".join([chr(ord(c1)^ord(c2)) for (c1, c2) in zip(text, key)])

with open("input.txt", "r") as file:
    s = file.readline()
s = s.split()
print("Результат программы:", enc_XOR(s[0], s[1]))