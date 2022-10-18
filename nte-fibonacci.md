# Funksjon som finner det nte Fibonacci-tallet (Python)

Vi begynner med å lage en liste, som inneholder de to første tallene i Fibonacci-rekka: 0 og 1:

`seq = [0, 1]`

Neste steg blir å legge sammen disse to, slik at vi får neste tall i rekka:  

`fib = seq[-1] + seq[-2]`

Legg merke til at vi legger sammen de to siste elementene i lista, `seq[-1]` og `seq[-2]`, fremfor de to første (`seq[0]` og `seq[1]`.  
Dette gjør at vi får rett løsning selv om lista blir lenger.  

Neste steg blir nå å legge til det nye fibonacci-tallet i lista:  

`seq.append(fib)`  

Vi har nå funnet neste tall i rekka, og lagt det til i lista.  
Denne oppskriften kan vi bruke for å finne så mange av de neste tallene som vi ønsker.  

```
seq = [0, 1]

n = 10

while len(seq) < n:
    fib = seq[-1] + seq[-2]
    seq.append(fib)

print(seq)
```

Dette gir oss `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`.

Vi wrapper alt i en funksjon, og returner bare de siste elementet i lista, som er `seq[-1]`:  

```
def nth_fibonacci(n):
    seq = [0, 1]

    while len(seq) < n:
        fib = seq[-1] + seq[-2]
        seq.append(fib)

    return seq[-1]

print(nth_fibonacci(250))
```

Output: `4880197746793002076754294951020699004973287771475874`
