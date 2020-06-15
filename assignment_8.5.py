fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line=line.strip()
    id=line.split()

    if len(id)<1:
        continue

    if id[0] == "From":
        print(id[1])
        count+=1

print("There were", count, "lines in the file with From as the first word")
