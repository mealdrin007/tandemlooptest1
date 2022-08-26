# Problem-4:  Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#     (examples)
#     input: [1,2,8,9,12,46,76,82,15,20,30]
#     Output:
#         {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
c=str(input("Enter list of number\n"))
d=c.strip("][").split(",")
b={}
for i in range(1,10):
    a=0
    for j in d:
        if (int(j))%i==0:
            a+=1
        else:
            pass
    b[i]=a
print(b)