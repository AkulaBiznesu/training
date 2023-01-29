from random import randint
a = int(input("a "))
b = int(input("b "))
n = int(input("n "))
count = 0
s = 0
for i in range(n):
    p = randint(a, b)
    if p % 3 != 0 and p in range(a, b):
        count += 1
        print(f"не ділиться {p}")
    else:
        s +=p
print(f"кількість не ділених на 3: {count}, сума решти: {s}")
