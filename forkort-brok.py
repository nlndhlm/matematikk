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


def forkort_brok(teller, nevner):

    t = primtallsfaktoriser(teller)
    n = primtallsfaktoriser(nevner)

    t.append(1) # legg til faktor 1 i teller-lista

    felles = [] # mellomlagring av felles verdier

    for p in t:
        if p in n:
            felles.append(p)

    for q in felles:    # fjerne felles faktorer i teller og nevner
        t.remove(q)
        n.remove(q)

    t_produkt = 1
    n_produkt = 1

    for r in t:
        t_produkt = t_produkt * r   # multiplisere verdier i teller-lista

    for s in n:
        n_produkt = n_produkt * s   # multiplisere verdier i nevner-lista




    return t_produkt, n_produkt

print(forkort_brok(16, 1024))