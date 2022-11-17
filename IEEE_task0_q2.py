x = input("Till which letter do you want the pattern to show up?(enter a capital letter) : ")




for i in range(65, (ord(x)+1)):
    print(chr(i), end="")

for i in reversed(range(65, ord(x))):
    print(chr(i), end = "")

print("", end = "\n")
#================================================================

cap = ord(x)-65-1
count = 0
while_count = 1

while count<=cap:
    for i in range(65, ord(x)-count):
        print(chr(i), end = "")

    while while_count<=(2*(count)+1):
        print(" ", end="")
        while_count = while_count+1

    for i in reversed(range(65, ord(x)-count)):
        print(chr(i), end = "")

    while_count = 1
    count = count+1
    print("", end = "\n")


count = cap-1
while count>=0:
    for i in range(65, ord(x)-count):
        print(chr(i), end = "")

    while while_count<=(2*(count)+1):
        print(" ", end="")
        while_count = while_count+1

    for i in reversed(range(65, ord(x)-count)):
        print(chr(i), end = "")

    while_count = 1
    count = count-1
    print("", end = "\n")

#====================================================

for i in range(65, (ord(x)+1)):
    print(chr(i), end="")

for i in reversed(range(65, ord(x))):
    print(chr(i), end = "")

print("", end = "\n")



