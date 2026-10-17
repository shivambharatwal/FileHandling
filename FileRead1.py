import os
if os.path.exists("practice1.txt"):
     with open("practice1.txt","r") as file:
        content= file.read()
        print(content)
else:
    print("File Doesn't exist")