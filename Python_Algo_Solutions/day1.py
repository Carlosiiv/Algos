# Reverse a String 
def rev(str):
    newstr = ""
    for i in range(len(str)-1 , -1 , -1):
        newstr += str[i]
    print(newstr)
rev("hello")

# Create an Acronym

def acronym(str):
    newacm = ""
    newacm += str[0]
    for i in range(len(str)):
        if str[i] == " ":
            newacm += str[i+1]
    print(newacm)
acronym("Laugh Out Loud")
        