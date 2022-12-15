with open('input.txt', 'r') as file:
    s = list(map(int, file.readline().split()))
s[0], s[1] = s[0]/2, s[1]/6
result = min(s)
if result < 1: result = 0
with open('output.txt', 'w') as file:
    file.write(str(int(result)))