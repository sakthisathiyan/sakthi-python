salary=int(input("enter your salary:"))
age=int(input("enter your age:"))
if(salary>=20000 or age<=25):
    loan=int(input("enter your required loan amount:"))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("maxium loan amount is 50000")
else:
    print("you are not eligible")
    
