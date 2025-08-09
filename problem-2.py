x=int(input("Enter a number until you need: "))
a=1
cnt=0
while cnt<x:
     if a%2!=0:
          print(a,end=' ')
          cnt+=1
     a+=1
