import random
l = ["O", "P"]
k = [0, 1, 0]
n = 0
s = 10
while s:
    x = random.randint(0, 1)
    k.append(x)
    for i in range(len(k)):
        if i + k[i+2]== 0:
            n += 1
            print("O")
            s-=1
            print(k)
        elif i + k[i+2] == 3:
            n += 1
            print("P")
            s-=1
            print(k)
    



# n = int(input('Введите число:'))
# while n:
#     x = random.randint(1, 2)
#     if x == 1:
#         print ('Орел')
#     else:
#         print ('Решка')
#     n -= 1