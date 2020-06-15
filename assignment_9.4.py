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
        id=words[1]
        final[id]=final.get(id,0) + 1

mail=None
count=None

for key, value in final.items():
    if count is None or value>count:
        mail=key
        count=value

print(mail, count)
