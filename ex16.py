# List of commands i want you to remember
# close - closes the file. like File->Save.. in your editor
# read - Reads the contents of the file . you can assign the result to a variaable.
# readline - Reads just one line of a text file.
# truncate - Empties the file. Watch out is you care about the file.
# write('stuff') - writes the "stuff" to the file.
# seek(0) - Move the read/write location to the begining of the file.
 
from sys import argv
 
script, filename = argv
 
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, Hit RETURN.")
 
input("?")
 
print("opening the file...")
target = open(filename,'w')
 
print("Truncating the file. Goodbye!")
target.truncate()
 
print("Now I'm going to ask you for three lines.")
 
line1 = input("line 1: ")  
line2 = input("line 2: ")
line3 = input("line 3: ")
 
print("Now I'm going to write these to the file.")
 
target.write(line1)
target.write("\n\t*")
target.write(line2)
target.write("\n\t*")
target.write(line3)
target.write("\n\t*")
 
print("And finally, we close it.")
target.close()
 