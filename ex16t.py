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
 
line1 = input('line 1: ')  
line2 = input("line2: ")
line3 = input("line3: ")

 
print("Now I'm going to write these to the file.")
 
target.write(line1+" \n"+ line2+" \n"+ line3)

 
print("And finally, we close it.")
target.close()