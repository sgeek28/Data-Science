import math

def isPrime(N):
	if math.gcd(N,2)==1:
		print("Prime")
	else:
		print("Not Prime")

num=int(input())
isPrime(num)