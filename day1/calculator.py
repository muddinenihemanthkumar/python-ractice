import math

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error: b cannot be zero"
    return a/b
def square(a):
    return a**2
def square_root(a):
    return math.sqrt(a)
def modulus(a,b):
    return (a%b)


while True :
    print("\n ------------calculator--------------")
    print(" 1. add")
    print(" 2. subtract")
    print(" 3. multiply")
    print(" 4. divide")
    print(" 5. square")
    print(" 6. square_root")
    print(" 7. Modulus")
    print(" 8. Exit")
    print(" Enter the choice: ")
    choice = int (input())
    print("\n")
    match choice:
        case 1:
             a=int(input("Enter a number: "))
             b=int(input("Enter another number: "))
             c=add(a,b)
             print(c)
        case 2:
            a=int(input("Enter a number: "))
            b=int(input("Enter another number: "))
            c=subtract(a,b)
            print(c)
        case 3:
            a=int(input("Enter a number: "))
            b=int(input("Enter another number: "))
            c=multiply(a,b)
            print(c)
        case 4:
            a=int(input("Enter a number: "))
            b=int(input("Enter another number: "))
            c=divide(a,b)
            print(c)
        case 5:
            a=int(input("Enter a number: "))
            c=square(a)
            print(c)
        case 6:
            a=int(input("Enter a number: "))
            c=square_root(a)
            print(c)
        case 7:
            a=int(input("Enter a number: "))
            b=int(input("Enter another number: "))
            c=modules(a,b)
            print(c)
        case 8:
            print("\nExiting calculator ")
            break
        case default:
            print("Invalid choice")
