import re
name=input("Enter file name: ")

nums=[]

with open(name, "r") as file_sample:
    for lines in file_sample:
        line=re.findall('[0-9]+', lines)

        if len(line)>0:
            for no in line:
                nums.append(int(no))

print("Sum=",sum(nums))
