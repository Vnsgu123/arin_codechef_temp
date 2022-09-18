N=int(input("Enter no of students       "))

i=0

l1=[]
l2=[]

while(i<N):
    name=input("Enter name")
    l1.append(name)
    total=input("Enter marks")
    l2.append(total)
    i=i+1

l3=l2[:]

l3.sort()

top=l3[N-1]

i=0
topper=[]
while(i<N):
    if(top==l2[i]):
        topper.extend(l1[i])
    i=i+1

topper.sort()

print(topper)