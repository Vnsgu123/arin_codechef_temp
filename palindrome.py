from audioop import reverse


T=int(input("Enter no of string         "))

j=0
str1=[]
str2=[]
while(j<T):
    
    str=input("Enter string     ")
    
    strr=str[::-1]
    
    str1.append(str)
    str2.append(strr)
    
    j=j+1
    
for j in range(len(str1)):
    if(str1[j]==str2[j]):
        print("Palindrome")
    else:
        print("Not Palindrome")