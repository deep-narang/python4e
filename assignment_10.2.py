name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

final=dict()

for line in handle:
    line=line.strip()
    words=line.split()

    if len(words)<1:
        continue

    if words[0] == "From":
        word=words[5]

        date=word.split(":")
        hour=date[0]

        final[hour]=final.get(hour,0) + 1

lst=list()
for key, value in final.items():
    lst.append( (key, value) )

lst=sorted(lst)

for key, value in lst:
    print(key, value)
