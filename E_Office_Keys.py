def find_min_time(n, k, room, people, keys):
    def is_possible(time):
        key_index = 0
        for person in sorted(people):
            if key_index >= k:
                return False
            while abs(sorted_keys[key_index] - person) + abs(sorted_keys[key_index] - room) > time:
                key_index += 1
                if key_index >= k:
                    return False
            key_index += 1
        return True

    sorted_keys = sorted(keys)

    left, right = 0, int(1e18)
    while left < right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    return left

n, k, room = map(int, input().split())
people = list(map(int, input().split()))
keys = list(map(int, input().split()))

result = find_min_time(n, k, room, people, keys)
print(result)