class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
a=float(input("Enter a 1st number: "))
b=float(input("Enter a 2nd number: "))
print("Select Operation:add / sub / mul / div")
operation=input("Enter operation: ")
cal=calculator()
if operation=='add':
    print('output: ',cal.add(a,b))
elif operation=='sub':
    print('output: ',cal.sub(a,b))
elif operation=='mul':
    print('output: ',cal.mul(a,b))
elif operation=='div':
    print('output: ',cal.div(a,b))
else:
    print("choose correct operation")
