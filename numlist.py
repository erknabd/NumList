import itertools

numbs = str(input("Which Numbers: "))
leng = int(input("Length: "))
save = str(input("File Name: "))

counter = 0
wlistfile = open(f"{save}","w")
for generate in itertools.product(numbs,repeat=leng):
    word= ("".join(generate))
    wlistfile.write(word)
    wlistfile.write('\n')
    counter+=1
print(f"{counter} words Wordlist created.")
