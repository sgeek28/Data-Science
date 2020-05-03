def printPattern(N):
	strm=''
	c=0
	no=-1
	for i in range(1,N+1):
		for j in range(1,N+1):
			if(j<N+1-c):	
				strm+=str(j)+' '
			elif(c>0 and j==N+1-c):
				m=no+c
				for k in range(1,m+1):
					strm+='*'+' '
		strm+='\n'		
		c=c+1;
		no=no+1
	
	print(strm)

	
n=int(input())
printPattern(n)
			
