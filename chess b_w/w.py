x = int(input("x: "))
y = str(input("y: ")).lower()

x_list = range(1, 9)
y_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

letter_index = y_list.index(y)
digit_index = x_list.index(x)

if letter_index % 2 == digit_index % 2:
    print('Black')
else:
    print('White')