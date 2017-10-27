convert = True
while convert:
    xkm = float(raw_input("vnesi kilometre za pretvorbo v milje"))
    p = 1.609
    xmil = xkm *  p
    print ("{0}km je {1}  mil").format(xkm, xmil)
    answer = raw_input("vtipkaj 'da' za novo pretvorbo ali 'ne' za konec:")

    if answer == 'da':
        continue
    elif answer == 'ne':
        convert = False
    else:
        raise ValueError("go fuck yourself")
