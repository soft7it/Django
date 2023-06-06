print() #\n

file = open('templates/header.html')
header = file.read()

file = open('templates/footer.html')
footer = file.read()

print(header)
print("<h1>Welcome to our Mini Social !!</h1>")
print(footer)
