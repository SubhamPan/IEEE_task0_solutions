x=input("How big do you want the star to be?(enter a positive integer greater than 4 to make it look good): ")
y=int(x)


for i in range(1,y+1):
    print("*", end = "")

print("", end = "\n")

count = 1

while count<=(y-2):
    for i in range(1,y-count):
        print(" ", end = "")

    print("*", end = "\n")
    count = count+1


for i in range(1,y+1):
    print("*", end = "")

