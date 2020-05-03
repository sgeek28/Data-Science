import sys
import math

def PrimeGenerator(l):
	length=len(l)
	for i in range(1,length,2):
		strn=''
		N=l[i]
		if N==1:
			N=N+1
		
		while N<=l[i+1]:
			flag=1
			j=2
			while j<=math.sqrt(N):
				#not prime
				if N%j==0:
					flag=0
					pass
				j=j+1
			if flag==1:
					#if prime then add
					strn+=str(N)+" "
				
			N=N+1
		print(strn)

strm=''
num=sys.stdin.readlines()
for item in num:
	strm+=item
number=[int(x) for x in strm.split()]
PrimeGenerator(number)
