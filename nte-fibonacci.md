# Funksjon som finner det nte Fibonacci-tallet (Python)

Vi begynner med å lage en liste, som inneholder de to første tallene i Fibonacci-rekka: 0 og 1:

`seq = [0, 1]`

Neste steg blir å legge sammen disse to, slik at vi får neste tall i rekka.  

`fib = seq[-1] + seq[-2]`

Legg merke til at vi legger sammen de to siste elementene i lista, `seq[-1]` og `seq[-2]`, fremfor de to første.




``
def nth_fibonacci(n):
    seq = [0, 1]

    while len(seq) < n:
        fib = seq[-1] + seq[-2]
        seq.append(fib)

    return seq[-1]

print(nth_fibonacci(250))
``
