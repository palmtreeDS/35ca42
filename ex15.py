# importing argument variables from system argv holds the arguments you pass to your python script when you run it
from sys import argv

# this line unpacks argv so that , rather than holding all the arguments, it gets assigned to two variables you can work with
script, filename = argv

# this is a new command open which takes a parameter and returns a value we can set our own variable,with this we can open a file
txt = open(filename)

print(f"Here's your file {filename}:")

# Here txt.read() says that "Hey txt! do your read command with no parameters!"
print(txt.read())

print("Type the filename again:")
# Here we are declaring a file name to be open by using input function
file_again =input("> ")

#Here we are opening the file which we are going to obtain from the input funtion that a user gives
txt_again = open(file_again)

#here we are printing the file from the user with no parameters
print(txt_again.read())
