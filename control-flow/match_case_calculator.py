num1=int(input("Enter the first number:  "))
num2=int(input("Enter the second number:  "))
operation=input("choose the operation (+,-,*,/) ")
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
match operation:
    case "+":
        print(f"the result is {addition}.")
    case "-":
        print(f" the result is {subtraction}.")
    case "*":
        print(f" the result is {multiplication}. ")
    case "/":
        if num2==0:
            print("cannot divide by zero.")
        else:
            print(f"the result is {num1/num2}.")
    case _:
        print("invalid operation.")
    


    






    
        

