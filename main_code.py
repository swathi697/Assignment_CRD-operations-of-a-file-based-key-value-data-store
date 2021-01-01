#this is for python 3.0 and above. use import thread for python2.0 versions
import time
import json

d={} #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key,value,timeout)" timeout is optional you can continue by passing two arguments without timeout
with open("Output_file.json","r") as JSON:
    d = json.load(JSON)
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for find operation
#use syntax "find(key)"
            
def find(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            print("         Given Key value is:",b[0])
            return stri

#for delete operation
#use syntax "delete(key)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            print(key," key is successfully deleted")
            del d[key]
            

#I have an additional operation of replace in order to change the value of key before its expiry time if provided

#for replace operation 
#use syntax "replace(key,value)"

def replace(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
def display():
    print(d)

#Creating a JSON by combining all the dictonaries

def creating_file():        
    json_object = json.dumps(d, indent = 4)
    with open("Output_file.json", "w") as outfile: 
        outfile.write(json_object)