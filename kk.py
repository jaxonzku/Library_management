a = "jithu"
b = "alesso"
c=len(a)
d=len(b)
if(c>d):
    greater=a
    lower=b
else:
    greater=b
    lower=a
for i in range(len(greater)):
    if(i>len(lower)-1):
        st=greater[i]
    else:
        st=greater[i]+lower[i]
    print(st)






    