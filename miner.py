import requests

def prime_factorisation(num):
    factors = []
    while num != 1:
        div = 2
        while div != num:
            if num % div == 0:
                factors.append(div)
                num /= div
            else:
                div += 1
        if div == num:
            factors.append(num)
            break
    return factors

def stupid(primes=[2,3], to_file=False, post=True):
    while True:
        new_primes = []
        i = 0
        while len(new_primes) < 2:
            factors = prime_factorisation((primes[0]*primes[1]+i)%2**25)
            i+=1
            if len(factors) == 1:
                new_primes.append(int(factors[0]))
        print(new_primes)
        primes = new_primes
        if post:
            data = {'host':'28033169680a075e33f020c0d3911693',
                    'p1':primes[0],
                    'p2':primes[1]}
            r = requests.post(url='https://webhook.site/194d7256-584c-4753-abd4-11a4cc9ce988', data=data)

        if to_file:
            f = open("./sample.primes", "a+")
            f.write(str(primes[0])+ " " + str(primes[1])+ "\n")
            f.close()



stupid(to_file=True)
