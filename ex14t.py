from sys import argv

script, user_name = argv
p = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"{user_name} I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(p)

print(f"Where do you live {user_name}?")
lives = input(p)

print("What kind of computer do you have?")
computer = input(p)

print("what kind of work do u do in your computer")
works = input(p)


print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
And you have a {computer} computer. Nice.
oh! really u use it for  {works} works.Great
""")