# f = open(r"C:\Users\User\Desktop\PythonPractice\17_File_Handling\hello.txt", "r")
# print(f.read())

with open(r"C:\Users\User\Desktop\PythonPractice\17_File_Handling\hello.txt", "r") as f:
    data = f.read()
    print(data)


print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()


# Handling Exceptions When Closing a File
try:
    f = open(r"C:\Users\User\Desktop\PythonPractice\17_File_Handling\hello.txt", "r")
    content = f.read()
    print(content)
finally:
    f.close()