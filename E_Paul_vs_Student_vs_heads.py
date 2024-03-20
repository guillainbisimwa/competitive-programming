def calculate_balance(city_a, city_b):
    if sum(city_a) != sum(city_b):
        return -1

    count = i = j = 0
    l_sum = city_a[i]
    r_sum = city_b[j]

    while i < len(city_a) - 1 and j < len(city_b) - 1:
        if l_sum == r_sum:
            count += 1
            i += 1
            j += 1
            l_sum = city_a[i]
            r_sum = city_b[j]
        elif l_sum < r_sum:
            i += 1
            l_sum += city_a[i]
        else:
            j += 1
            r_sum += city_b[j]
    i += 1
    j += 1
    while i < len(city_a):
        l_sum += city_a[i]
        i += 1

    while j < len(city_b):
        r_sum += city_b[j]
        j += 1

    if l_sum == r_sum:
        count += 1
        return count
    else:
        return -1

def main():
    n = int(input())
    city_a = list(map(int, input().split()))
    m = int(input())
    city_b = list(map(int, input().split()))

    balance = calculate_balance(city_a, city_b)
    print(balance)

if __name__ == "__main__":
    main()
