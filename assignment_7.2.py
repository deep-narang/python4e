# Use the file name mbox-short.txt as the file name
count=0
add=0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(":")
        no=str(line[pos+1:])
        no=no.strip()
        no=float(no)

        add+=no
        count+=1

print("Average spam confidence:", add/count)
