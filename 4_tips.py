#73
a = str(input("word "))
b = int(input("symbols "))
new_message = ""
for i in a:
    
    if i >= "a" and i<= "z":
        pos = ord(i) - ord("a")
        pos = (pos+b) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    
    elif i >= "A" and i <= "Z":
        pos = ord(i) - ord("A")
        pos = (pos + b) % 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    
    else:
        new_message = new_message + i

print("Новое сообщение", new_message)
print(new_message)