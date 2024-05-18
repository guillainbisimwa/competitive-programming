def checkGreaterThan10(array):
	"""
	FOR [8,1,2] the answer is YES
	FOR [4,4,5] the answer is NO

	--------------Approach------------
	for [8,1,2]
	step1 test if he value in index 0 + value in dex 1 >= 10 the return YES
	elif value in index 0 + value in index 1 >= 10 the return YES
	elif value in index 1 + value in index 2 >= 10 the return YES
	else return NO

	------------ Solution --------------
	step1 :
	[8,1]
	[8]
	(recursion?)

	return checkGreaterThan10recusrion(a,b)
	return checkGreaterThan10recusrion(a,c)
	return checkGreaterThan10recusrion(b,c)

	"""		
	n = len(array)
	array.sort()
	# index = len(array)
	for i in range(n):
		for j in range(n):
			if i != j:
				if array[i-1] + array[j-1] >= 10:return "YES"
			
		return "NO"


t = int(input())
for _ in range(t):
    abc = list(map(int, input().split()))
    print(checkGreaterThan10(abc))
    #checkGreaterThan10(abc)