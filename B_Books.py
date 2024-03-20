def get_input():
    num_books, available_time = map(int, input().split())
    num_minutes = list(map(int, input().split()))
    return num_books, available_time, num_minutes

def find_max_books(num_books, available_time, num_minutes):
    max_books = 0
    left, sum_time = 0, 0

    for right in range(len(num_minutes)):
        sum_time += num_minutes[right]

        while left <= right and sum_time > available_time:
            sum_time -= num_minutes[left]
            left += 1
        
        max_books = max(max_books, right - left + 1)

    return max_books

def main():
    num_books, available_time, num_minutes = get_input()
    max_books = find_max_books(num_books, available_time, num_minutes)
    print(max_books)

if __name__ == "__main__":
    main()