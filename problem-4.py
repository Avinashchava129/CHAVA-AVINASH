numbers=[1,2,8,9,12,46,76,82,15,20,30]
result={}
for i in range(1,10):
    cnt=0
    for num in numbers:
        if num%i==0:
            cnt+=1
        result[i]=cnt
print(result)
