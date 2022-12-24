# funksjon som primtallsfaktoriserer et tall

def primtallsfaktoriser(tall):

    i = 2

    faktorer = []

    while i <= tall:
        if tall % i == 0:
            faktorer.append(i)

            tall = tall / i
            i = 2

        else:
            i = i + 1

    faktorer.sort(reverse=True) # sorterer i stigende rekkerfølge

    return faktorer

print(primtallsfaktoriser(49))