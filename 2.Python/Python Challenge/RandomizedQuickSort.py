import sys
import random


def printList(a):
	strn=''
	for item in a:
		strn+=str(item)+' '
	return strn


def swap(a,p1,p2):
	a[p1],a[p2]=a[p2],a[p1]
	return a

def Partition(a,p,q):
	x=a[q]
	i=p-1
	for j in range(p,q):
		if a[j]<=x:
			i=i+1
			swap(a,i,j)
	swap(a,i+1,q)
	return i+1

def RandomPartition(a,p,q):
	r=random.randrange(p,q)
	swap(a,p,r)
	return Partition(a,p,q)

def QuickSort(a,p,q):
	
	if(p<q):
		mid=RandomPartition(a,p,q)
		QuickSort(a,p,mid-1)
		QuickSort(a,mid+1,q)


strm=''
num=sys.stdin.readlines()
for item in num:
	strm+=item
a=[int(x) for x in strm.split()]
#to pop first line input which is nothing but size of list
length=a.pop(0)
QuickSort(a,0,length-1)
print(printList(a))