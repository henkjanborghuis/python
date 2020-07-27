filename = 'name.txt'
content = ''
# name = input('You can type your name here:    ')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    content += line

print(content)
