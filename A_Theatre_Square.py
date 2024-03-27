def theatre_square(n, m, a):
    rows = n // a
    cols = m // a
    rows += n % a > 0
    cols += m % a > 0 
    
    return rows * cols
        
n, m, a = map(int, input().split())

number_of_flagstones = theatre_square(n, m, a)
print(number_of_flagstones)
