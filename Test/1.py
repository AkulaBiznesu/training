x = ["agh", "bc", "cef", "vb", "asdfgk"]
s = { i : len(x[i]) for i in range(0, len(x))}
for i in range(len(s), 0, -1):
    print(i)

print(s)