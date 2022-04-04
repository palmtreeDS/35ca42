# Assigning a string to variable x ,and using formatters  inside the string
x = "There are %d types of people." % 10
#Assigning binary value to binary variable
binary = "binary"
#Assigning the don't value the variable do_not
do_not = "don't"
# Assigning a string to a variable y, and use of formatters inside the string
y = "Those who jnow %s and those who %s." % (binary,do_not)

# next two statements are about the printing of variable x,y.

print x
print y

#These two statements are about printing the srings including other values by using the formatters
print "I Said: %r." % x
print "I also said: '%s'." % y


#Declaring a Boolean value to the variable hilarious,
hilarious = False
#Declaring a string to a variable joke_evaluation
joke_evaluation = "Isn,t that joke so funny ?! %r"

# printing of one variable by print function and including other variable by % formatter
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w+e
