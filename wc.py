

t=int(input("ENTER NO OF STRING     "))
wc=int(0)
j=0
# for j in t:
while(j < t):
    str=input("ENTER STRING     ")
    for i in range(0,len(str)):
        wc=wc+1 
        if(str[i]==" "):
            print(wc-1)
            wc=0
        elif(str[i]=='@'):
            wc=0
    print(wc)
    j=j+1
    


# print(i)