def planet(n):
    pl, des = map(int, input().split())
    orbits = list(map(int, input().split()))

    orbit_count = {}
    for orbit in orbits:
        if orbit in orbit_count:
            orbit_count[orbit] += 1
        else:
            orbit_count[orbit] = 1
    
    total_cost = 0
    for orbit in orbit_count:
        count = orbit_count[orbit]
        cost_using_first_machine = count
        cost_using_second_machine = des
        total_cost += min(cost_using_first_machine, cost_using_second_machine)
    
    print(total_cost)

n = int(input())

for _ in range(n):
    planet(n)

# 10 1
# 2 1 4 5 2 4 5 5 1 2