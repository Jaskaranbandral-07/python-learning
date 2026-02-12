#Simple Dynamic calculator :
#defining functions :
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    #zero cannot be in denominator
    if b==0:
        return("Given value cannot be divided by zero")
    return a/b
#Selecting operators :
print("Select an operator :")
print(f"1. ADD")
print(f"2. SUB")
print(f"3. MULTIPLY")
print(f"4. DIVISION")

flag = True
#conditons for the operators defined :
while flag:
    choice = input("Enter Your Operation (1/2/3/4) : ")
    if choice in ('1','2','3','4'):
        try:
            a=float(input("Enter Your First Value :"))
            b=float(input("Enter Your Second Value :"))
        except ValueError:
            print("Invalid Input.Try Again with Numeric Values")
            continue
        if choice=='1':
            print(add(a,b))
        elif choice =='2':
            print(sub(a,b))
        elif choice =='3':
            print(multiply(a,b))
        elif choice =='4':
            print(divide(a,b))
        
        next_calculation = input("Do next Calculation [Yes/No] : ")
        if next_calculation.lower() != 'yes':
            flag = False
        else:
            continue