import heapq

def find_challenge_exceeding_time():
    t = int(input())
    results = []

    for _ in range(t):
        _, available_time = map(int, input().split())
        challenge_times = list(map(int, input().split()))
        total_time_needed = sum(challenge_times)

        if available_time >= total_time_needed:
            results.append(0)
            continue

        current_time = 0
        max_heap = []
        failed_challenge = 0

        for idx, challenge_time in enumerate(challenge_times):
            current_time += challenge_time
            heapq.heappush(max_heap, (-challenge_time, idx))

            if current_time > available_time:
                m, challenge_idx = heapq.heappop(max_heap)
                failed_challenge = challenge_idx + 1
                break

        results.append(failed_challenge)

    for result in results:
        print(result)

# Run the function
find_challenge_exceeding_time()
