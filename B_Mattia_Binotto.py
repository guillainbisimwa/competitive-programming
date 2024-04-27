def max_not_disappointed_drivers(n, pit_stop_times):
    pit_stop_times.sort()
    max_drivers = 0
    wait_time = 0
    
    for pit_stop_time in pit_stop_times:
        if pit_stop_time > wait_time:
            max_drivers += 1
        wait_time += pit_stop_time
    
    return max_drivers

n = int(input().strip())
pit_stop_times = list(map(int, input().strip().split()))

result = max_not_disappointed_drivers(n, pit_stop_times)

print(result+1)
