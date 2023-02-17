#  EXERCISE - SECRET CODE LANGUAGE :--------------- 

# Write a python program to translate a message into secret code language. Use the Rules below to translate normal Enlgish into secret code language.

''' Rules : ---------
Coding :----------

1. If the word contains atleast 3 characters, remove the first letter and append if at the end. 
2. Now append three random characters at the starting and the end 
else:
    simply reverse the string.
    
'''
try:
    while True:
            
            def EncName(name):
                print(name)
                a = list(name)
                string = []               
                if(len(name)>=3):
                #Removing first character of name string. 
                    s = a.pop(0)
                # Adding 3 random character at the begin.
                    for i in range(3):
                        b = input("Enter the character : ")
                        string.append(b)
                #Adding remain name character in string list.
                    for i in a:
                        string.append(i)
                #Adding first character of the name in last.
                    string.append(s)
                #Adding 3 random charcter in the last. 
                    for i in range(3):
                        c = input("Enter the character :")
                        string.append(c)
                    
                # Printing  the encrypted code : ------
                    Ename = ""
                    Ename = Ename.join(string)
                    
                    return print(Ename)

       
            choice = int(input('''
                1 For Coding |
            
                2 For Exit  |
                        
        Enter you choice :  ''' ))
            if(choice == 1):
                name = input("Enter you name : ")
                EncName(name)        
           
            elif(choice == 2):
                break

except:
    print("The error occured.....")