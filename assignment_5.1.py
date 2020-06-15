smallest=None
largest=None

while True:
    number=input("Enter a Number:")

    if number == "done":
        break

    try:
        no=int(number)
    except:
        print("Invalid input")
        continue

    if smallest is None and largest is None:
        smallest=no
        largest=no

    if no>largest:
        largest=no

    if no < smallest:
        smallest = no

print("Maximum is", largest)
print("Minimum is", smallest)
