dictionary = {}
keysortDictionary = {} #empty dictioary in which i will store the keys in a sorted manner
valuesortDictionary = {} #empty dictioary in which i will store the keys in a sorted manner



#number of keys in the dictionary
n = int(input("Enter the number of keys in the dictionary: "))


#inputting keys and values of the dictionary
for i in range(0,n):
    key = input("Enter a key: ")
    value = input("Enter a value: ")

    dictionary[key] = value




#function for KEY-sorting a dictionary
def keysort(dictionary, keysortDictionary):
    for i in sorted(dictionary):
        keysortDictionary[i] = dictionary[i]


#calling the above function
keysort(dictionary, keysortDictionary)
#printing the KEY-sorted dictionary
print("Key sorted dictionary: ")
print(keysortDictionary)





#function for VALUE-sorting a dictionary
def valuesort(dictionary, valuesortDictionary):
    for i in sorted(dictionary.values()):
        valuesortDictionary[list(dictionary.keys())[list(dictionary.values()).index(i)]] = dictionary[list(dictionary.keys())[list(dictionary.values()).index(i)]]







#calling tha above function
valuesort(dictionary, valuesortDictionary)
#printing the VALUE-sorted dictionary
print("Value sorted dictionary: ")
print(valuesortDictionary)







