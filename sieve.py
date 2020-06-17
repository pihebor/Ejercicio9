def primes(limit):
    var = []
    primo = []
    if limit < 2:
        return primo
    else:
        x = 2
        while x <= limit:
            if x not in primo and x not in var:
                primo.append(x)
            
            k = x
            while k <= limit:
                k += x
                var.append(k)

            x += 1

        return primo
