def dig_pow(n, p):
    digits = [int(x) for x in str(n)]
    list_p = []
    toplam = []
    for t in range(p,p+len(digits)):
        list_p.append(t)
    for i in range(len(digits)):
        toplam.append(digits[i]**list_p[i])
    k = sum(toplam)
    if (k%n == 0):
        return int(k/n)
    else:
        return -1