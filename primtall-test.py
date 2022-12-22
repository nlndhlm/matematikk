def primtall_test(n):
    i = 2

    while i < n:
        if (n % i) == 0:
            return (False) # False hvis n ikke er primtall
        else:
            i += 1

    return True # True hvis n er primtall

print(primtall(2987549734857))