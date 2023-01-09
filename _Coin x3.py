import random
l = ["O", "P"]
k = []
count = 0
s = 10
while s:
    x = random.randint(0, 1)
    k.append(x)
    for i in range(len(k)-2):
        if k[i] + k[i+2] == 0:
            print("O")
            print(k)
        elif k[i] + k[i+2] == 2:
            print("P")
            print(k)
            s-=1



# n = int(input('Введите число:'))
# while n:
#     x = random.randint(1, 2)
#     if x == 1:
#         print ('Орел')
#     else:
#         print ('Решка')
#     n -= 1