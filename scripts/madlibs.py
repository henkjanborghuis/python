def new_line():
    print("\n")

print("Hi dude! Let's play MadLibs!")
new_line()
words = input("Provide a verb, noun and adjective:   ")
verb, noun, adjective = words.split(" ")
new_line()
print("I enjoy practice! I find it helps me to {} better.".format(verb))
print("Without practice, my {} would probably not even work.".format(noun))
print("My code is getting more {} every single day!".format(adjective))
new_line()
