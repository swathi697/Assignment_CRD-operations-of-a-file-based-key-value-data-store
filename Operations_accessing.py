#here are the commands to demonstrate how to access and perform operations on a main file

from threading import*
#run the MODULE of MAIN FILE and import mainfile as a library 

import main_code as x 
import json
#importing the main file("code" is the name of the file I have used) as a library 



#x.create("sastra",25)
#to create a key with key_name,value given and with no time-to-live property


#x.create("src",703600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


#x.read("sastra")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


#x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


#x.create("sastra",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


#x.modify("sastra",55)
#it replaces the initial value of the respective key with new value 

 
#x.delete("sastra")


while(True):
    print("Enter 1 for Insert, 2 for Find, 3 for Replace, 4 for Delete, 5 for Exit :\n")
    n=int(input("Enter the Number :"))
    if(n==1):
        s1=input("Enter the key for create :")
        s2=int(input("Enter the Value for create :"))
        s3=int(input("Enter the Time to live value :"))
        x.create(s1,s2,s3)
    elif(n==2):
        s1=input("Enter the Key for Finding its value :")
        x.find(s1)
    elif(n==3):
        s1=input("Enter the Key for replace :")
        s2=int(input("Enter the Value for replace :"))
        x.replace(s1,s2)
    elif(n==4):
        s1=input("Enter the Key for delete :")
        x.delete(s1)
    elif(n==5):
        break
x.display()
x.creating_file()
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like

#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

