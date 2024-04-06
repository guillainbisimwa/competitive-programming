def find_car(n, enter, out):
    fined = 0
    max_out = [0] * (n + 1)
    max_in = 0

    for i in range(n):
        current_exit = out[i]
        max_out[current_exit] = i

    for i in range(n):
        current_in = enter[i]

        if max_out[current_in] < max_in:
            fined += 1
        else:
            max_in = max(max_in, max_out[current_in])
    
    print(fined)


n = int(input())
enter = list(map(int, input().split()))
out = list(map(int, input().split()))

find_car(n, enter, out)
