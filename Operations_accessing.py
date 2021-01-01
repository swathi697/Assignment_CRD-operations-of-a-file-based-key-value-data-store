#here are the commands to demonstrate how to access and perform operations on a main file
import main_code as x 
import json
#importing the main file("main_code" is the name of the file I have used) as a library 


while(True):
    print("Enter 1 for Insert, 2 for Find, 3 for Replace, 4 for Delete, 5 for Exit :\n")
    n=int(input("Enter the Number :"))
    if(n==1):
        s1=input("Enter the key for create :")
        s2=int(input("Enter the Value for create :"))
        s3=int(input("Enter the Time to live value :"))
        x.create(s1,s2,s3)      #it creates the respective key and its value from the database(memory is also freed)
    elif(n==2):
        s1=input("Enter the Key for Finding its value :")
        x.find(s1)      #it returns the value of the respective key in Jasonobject format 'key:value'
    elif(n==3):
        s1=input("Enter the Key for replace :")
        s2=int(input("Enter the Value for replace :"))
        x.replace(s1,s2)    #it replaces the initial value of the respective key with new value 
    elif(n==4):
        s1=input("Enter the Key for delete :")
        x.delete(s1)      #it deletes the respective key and its value from the database(memory is also freed)
    elif(n==5):
        break
x.display()
x.creating_file()

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

