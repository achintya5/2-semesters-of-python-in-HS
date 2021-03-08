#collatz sequence

def collatz(number):
    if number%2==0:
        number/=2
        print(number, 'even condition result', sep="--")
        return number
    else:
        number = number*3 +1
        print(number, 'odd condition result', sep="--")
        return number

r = collatz(int(input("Enter an integer here: ")))

while r != 1:
    r = collatz(r)

