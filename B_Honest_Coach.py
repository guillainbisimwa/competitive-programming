
def honestCoach(n,a):

    #[1,2,3,4,6]
 
    a.sort()
    minumum_dif = float('inf') # infinit
    

    for i in range(1, n):
        diff = a[i] - a[i - 1]
        minumum_dif = min(minumum_dif, diff)
    
    print(minumum_dif)


t = int(input())
for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().split()))
    honestCoach(n, strengths)

