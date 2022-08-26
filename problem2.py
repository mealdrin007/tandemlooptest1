# Problem-2:  With a single integer as the input, generate the following until a = x [series of numbers as shown in the below examples]
#
#     Output: (examples)
#         1) input a = 1, then output : 1
#         2) input a = 2, then output : 1, 3
#         3) input a = 3, then output : 1, 3, 5
#         4) input a = 4, then output : 1, 3, 5, 7
#         .
#         .
#         5) input a = x, then output : 1, 3, 5, 7, .......

while True:
    a=int(input("a="))
    b=a*2
    c=""
    for i in range(b):
        if i==1:
            c+=str(i)
            if (i+1)!=b:
                c+=","
        elif i%2!=0:
            c+=str(i)
            if (i+1)!=b:
                c+=","
        else:
            pass
    print(c)