from random import randint
a = int(input("a "))
m = 0
l = 0
s = 0
for i in range(-a, a):
    p = randint(-a, a)
    print(p)
    if p == 0:
        print("zero 0")
        break
    elif p <0:
        m += p
    elif p > 0 and p < a and p >l:
        l = p
    elif p < s and p > -a:          #problem
        s = p

print(f"maximum: {l}, lowest: {s}, sum of negative: {m}")
