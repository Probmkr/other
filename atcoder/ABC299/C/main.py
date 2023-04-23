n = int(input())
s = input()

if (not ("-" in s and "o" in s)):
    print(-1)
else:
    print(len(max(s.split("-"))))
