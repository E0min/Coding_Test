answer = "asdf asdf df"
li = answer.split(' ')

for i in li:
    i[0].upper()
    i[1:-1].lower()
    
print(li)