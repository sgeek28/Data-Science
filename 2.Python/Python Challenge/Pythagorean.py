import sys
import math

def PythagoreanPairs(l):
	length=len(l)
	for j in range(1,length):
		strn=''
		sum=0
		sqroot=math.sqrt(l[j])
		if sqroot.is_integer():
			strn+="(0,"+str(int(sqroot))+")"+" "
			a=1
			b=a
			i=a
			while i<=int(sqroot) and a<=b:
				sum=a**2+b**2
				if sum==l[j]:
					strn+="("+str(a)+","+str(b)+")"+" "
				elif i==int(sqroot) and a<=int(sqroot):
					i=a
					a=a+1
				else:
					pass
				i=i+1
				b=i
		print(strn)

strm=''
num=sys.stdin.readlines()
for item in num:
	strm+=item
lst=[int(x) for x in strm.splitlines()]
PythagoreanPairs(lst)