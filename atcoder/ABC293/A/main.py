s = input()
r = ""
for i in range(0, len(s), 2):
    r += f"{s[i+1]}{s[i]}"
print(r)
