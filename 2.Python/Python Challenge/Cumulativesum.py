import sys
def CumSumNegative(l):
	i=0
	sum=0
	while(sum>=0):
		sum+=l[i]
		i=i+1
	for m in range(0,i-1):
		print(l[m])

strm=''
n=sys.stdin.readlines()		
for item in n:
	strm+=item
num=[int(no) for no in strm.splitlines()]
CumSumNegative(num)
