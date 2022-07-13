
"""
This funtion will convert a decimal number 
to binary number and return the binary number
"""
def decimal_binary(num):
    binary = ""
    while num !=0:
        rem = num%2
        binary += str(rem)
        num //= 2
    return binary[::-1]

print(decimal_binary(10))