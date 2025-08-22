# print("hello sonu bh hero")
# li =[1,2,3,4,5]
# min=li[4]
# max=li[0]
# for i in li:
#     if i > max:
#         max=i
#     elif i<min:
#         min=i
# print(max)
# print(min)        

n = int(input(("Enter your number:")))
for i  in range(n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    # print star
    for k in range(2*i-1):
        print("*",end=" ")
    print()