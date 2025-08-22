
# string to integer
s =['1','2','3','4','5']
result=map(int,s)
print(list(result))

# Converting Map object into list
a =[2,4,6,7,8]

def double(val):
    return val*2

res =list(map(double,a))
print(res)

# map with lambda function
m=[2,3,4,5,6]
ans =map(lambda x :x*2,m)
print(list(ans))

# map with multiple Expression
a1 =[1,2,3,4]
b1 =[5,6,7,8]
ans1 =map(lambda x,y:x+y,a1,b1)
print(list(ans1))

# Converting String to upper case
s1 =["hello","guys","how","are","you"]
UpperString =list(map(lambda x:x.upper(),s1))
print(UpperString)

# Extracting First Character from the String
s2 =["apple","mango","banana"]
extractStr=list(map(lambda x:x[0],s2))
print(extractStr)

# Removing whitespaces from strings
s3 =['  hello   ' , '  World ' , ' python ']
removeSpace =list(map(str.strip,s3))
print(removeSpace)

# Calculate fahrenheit from celsius
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))

