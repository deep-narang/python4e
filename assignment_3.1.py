hrs = input("Enter Hours:")
h = float(hrs)
rph=float(input("Enter rate per Hour:"))

if h<=40:
    pay = rph * h

else:
    #calculating the extra hours after 40 hrs
    left = h-40
    h-=left
    rph_after= rph * 1.5

    #pay_less = upto 40 hrs and pay_after= after hours
    pay_less= rph * h
    pay_after= rph_after * left

    pay= pay_after + pay_less

print(pay)
