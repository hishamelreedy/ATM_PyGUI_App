def SET_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR | (1 << BIT)
	return result
	
def CLR_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = VAR & (~(1 << BIT))
	return result
	
def GET_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result = (VAR >> BIT) & 1
	return result
	
def TOG_BIT(VAR,BIT):
	VAR = int(VAR)
	BIT = int(BIT)
	result =VAR ^ (1 << BIT) 
	return result

n=13;
for i in range(n):
    for j in range(i):
        print ('*', end=" ")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('')





