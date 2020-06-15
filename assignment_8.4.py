name=input("Enter file name:")
fhandle=open(name, "r")

final=list()

for lines in fhandle:
    lines=lines.strip()

    line=lines.split()

    for word in line:
        if not word in final:
            final.append(word)

final.sort()
print(final)
