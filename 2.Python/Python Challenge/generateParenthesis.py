def genParenthesis(openB,closeB,n,s=[]):
	if(closeB==n):
		print(''.join(s))
		return 

	else:
		if(openB>closeB):
			s.append(')')
			genParenthesis(openB,closeB+1,n,s)
			s.pop()
		
		if(openB<n):
			s.append('(')
			genParenthesis(openB+1,closeB,n,s)
			s.pop()
	return


n=int(input())
genParenthesis(0,0,n)