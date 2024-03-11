# Python can be used to perform operations on a file, i.e., read & write data

# Types of all files:
# 1.Text files: .txt, .docx,.log etc.
# 2. Binary files: .mp4, .mov, .png, .jpeg etc.  

# At the end all files are stored in bits i.e., 0 and 1

# To open a file
# f = open("file_name", "mode") # mode means what are we going to do after opening the file, by default python assures read mode.

# f = open("demo.txt", "r") # opens and read the file
# data = f.read() # reads entire file
# print(data)
# print(type(data))

# # Reset file cursor to the beginning for reading lines again
# f.seek(0)

# data2 = f.readline() # reads one line at a time
# print(data2)

# # Reset file cursor to the beginning for reading lines again
# f.seek(0)

# data3 = f.read(5) # In this it will only read 5 characters
# print(data3)

# f.close() # closes the file

# Writing to a file
file = open("demo.txt", "w")

file.write("This is a new line, it will replace the older content.") # overwrites the entire file

file = open("demo.txt", "a")

file.write(" This is the line that is getting appended") # appends the content at the end

file.close()

# with Syntax

with open("demo.txt", "r") as f:
  data = f.read()
  print(data)
  # with syntax automatically closes the file

# Deleting a file

# import os
# os.remove("demo.txt")