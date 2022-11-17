distinctIntegersListInput = []

n = int(input("Enter number of distinct integers, and then the disctinct integers themselves: "))

for i in range(0, n):
    distinctIntegers = int(input())
    distinctIntegersListInput.append(distinctIntegers)

#================================================
print("[]")


#=================================================

print("[", end = "")
for i in range(0,n-1):
    print(distinctIntegersListInput[i], end = ", ")

print(distinctIntegersListInput[n-1], end = "]")

