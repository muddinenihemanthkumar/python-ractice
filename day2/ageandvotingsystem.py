#age and voting system
def check(age,citizen):
    if citizen.lower() =="y":
        if age>=18:
            return True
        else:
            return False
    else:
        return False

name=input("Enter your name: ")
age=int(input("Enter your age: "))
citizen=input("Are you a citizen? y/n: ")
if check(age,citizen):
    print(f"{name} is eligible for voting")
else:
    print(f"{name} is not eligible for voting")
check=lambda age,citizen: "eligible" if age>=18 and citizen.lower()=="y" else "not eligible"