def computepay(hrs, rph):
    pay=0
    if hrs>40:
        left= hrs-40
        hrs-=left

        ro= rph * 1.5
        pb= rph * hrs
        pa= ro * left
        pay= pa + pb

    else:
        pay= rph * hr
    return pay

hrs=float(input("Enter Hours:"))
rph= float(input("Enter Rate per Hour:"))

print("Pay",computepay(hrs, rph))
