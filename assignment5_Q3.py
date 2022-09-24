number = 76542
copynumber = number
reversenumber = 0
while copynumber > 0:
    x = copynumber % 10
    reversenumber = (reversenumber * 10) + x
    copynumber = copynumber // 10
print("number:", number, "revere number:", reversenumber)