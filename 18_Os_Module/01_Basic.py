import os

# Get current working directory
print("Current Directory:", os.getcwd())

# Change directory
# os.chdir("C:/Users/User/Desktop")

# List files in current directory
print("Files:", os.listdir())

# Create a new folder
os.mkdir("new_folder")

# Remove a folder
os.rmdir("new_folder")

# Join paths (safe for all OS)
path = os.path.join("C:", "Users", "User", "Desktop", "file.txt")
print("Joined Path:", path)

# Check if file exists
print(os.path.exists("hello.txt"))
