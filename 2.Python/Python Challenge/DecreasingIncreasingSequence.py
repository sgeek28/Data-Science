import sys

def IsSortedArray(l):
	c=0
	i=1
	length=l[0]
	while i<length:
		if l[i]>l[i+1] and c==0:
			pass
		elif l[i]<l[i+1]:
			c=1
			pass
		else:
			print("false")
			return
		i=i+1
	print("true")

strm=''
num=sys.stdin.readlines()
for item in num:
	strm+=item
lst=[int(x) for x in strm.splitlines()]
IsSortedArray(lst)

			