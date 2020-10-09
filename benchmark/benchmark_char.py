## https://stackoverflow.com/questions/16308989/fastest-method-to-generate-big-random-string-with-lower-latin-letters

from  random import random, getrandbits
import time

def test_one(N):
    a = 0
    t0 = time.time()
    for i in range(N):
        if getrandbits(1):  a += 1

    return time.time() - t0

def rand_bools_int_func(n):
    r = getrandbits(n)
    return ( bool((r>>i)&1) for i in range(n) )

def test_generator(gen):
    a = 0
    t0 = time.time()
    for b in gen:
        if b:  a += 1
    return time.time() - t0

def test_random(n):
    t0 = time.time()
    a = [random() >=0.5 for _ in range(n)]

    print(a)

    return time.time() - t0

def test(N):
    print('For N={0}'.format(N))
    print('  getrandbits(1) in for loop              {0} sec'.format(test_one(N)))
    print('  random() >= 0.5 in for loop              {0} sec'.format(test_random(N)))



    gen = ( not getrandbits(1) for i in range(N) )
    print('  getrandbits(1) generator using not      {0} sec'.format(test_generator(gen)))

    gen = ( bool(getrandbits(1)) for i in range(N))
    print('  getrandbits(1) generator using bool()   {0} sec'.format(test_generator(gen)))

    # if (N < 10**6):     # Way too slow!
    #     gen = rand_bools_int_func(N)
    #     print('  getrandbits(n) with shift/mask          {0} sec'.format(test_generator(gen)))

def main():
    for i in range(3,8):
       test(10**i)

if __name__ == '__main__':
   main()