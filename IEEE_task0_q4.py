inputtedBinaryNumber_stringFormat = input("Enter a binary number: ")
inputtedBinaryNumber_intFormat = int(inputtedBinaryNumber_stringFormat)

def BinaryToDecimal(s):
    n = len(s)
    x = int(s)
    count = n
    sum = 0
    intermediate = 0
    digit = 0
    i = 0
    while(count>=1):
        intermediate = (x//10**(count-1))
        digit = intermediate - (x//10**(count))*(10)
        sum = sum + digit*(2**(count-1))
        i=i+1
        count = count-1
    
    return sum
    
    

decimalForm = BinaryToDecimal(inputtedBinaryNumber_stringFormat)



def DecimalToRomanPrintFunction(number):
    decimalVersion = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romanVersion = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i=12
    while number>0:
        quotient = number // decimalVersion[i]
        number = number%(decimalVersion[i])

        while quotient>0:
            print(romanVersion[i], end = "")
            quotient -= 1
        i -= 1
    
    
DecimalToRomanPrintFunction(decimalForm)










