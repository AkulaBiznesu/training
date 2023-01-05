proc = 0.12
suma = float(input("how much did you put on your account?: "))
first = suma + (suma*proc) 
second = first * proc + first
third = second * proc + second
print(f"first year: {round(first, 2)}, second year: {round(second, 2)}, third year: {round(third, 2)}")
