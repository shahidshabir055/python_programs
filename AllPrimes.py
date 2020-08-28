# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:07:57 2020

@author: eshah
#find all the prime numbers between two given numbers
"""
"""
def findPrime(N):
    primes=[]
    is_prime=[False,False]+[True]*(N-1)
    for p in range(2,N+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p,N+1,p):
                is_prime[i]=False
    return primes
N=10
print(findPrime(N))
"""
def findPrimes(N):
    primes = []
    for i in range(1, N):
        if i == 1:
            continue
        flag = 1
        for j in range(2, (i//2)+1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            primes.append(i)
    return primes
N=100
print(findPrimes(N))