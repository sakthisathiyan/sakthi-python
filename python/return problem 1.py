s_username="sakthi"
s_password="123"

username=input("enter value for username:")
password=input("enter value for password:")
def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)
    
    

    
