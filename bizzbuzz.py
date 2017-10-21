x = int(raw_input("vnesi stevilo: "))
for i in range(x):
    if i % 3 == 0 and i % 5 ==0:
        print "fizzbuzz"
    elif i % 5 == 0:
        print "buzz"
    elif i % 3 == 0:
        print "fizz"
    else:
        print i


