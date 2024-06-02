n, q = map(int, input().split())
a = list(map(int, input().split()))
l = [a[0]]
for i in range(n-1):
	A, B = l[i], a[i+1]
	if A<B: A,B = B,A
	l.append(A)
	a.append(B) 
for i in range(q):
	m = int(input())
	if m <= n:
		print(l[m-1], a[m])
	else:
		print(l[-1], a[n + (m-n)%(n-1)])