def score_high(m):
    results = []
    for t in m:
        n, k, z, arr = t
        score_high = 0
        
        for left_moves in range(z + 1):
            remaining_moves = k - 2 * left_moves
            if remaining_moves < 0:
                continue
            
            current_score = sum(arr[:remaining_moves + 1])
            
            max_pair = 0
            for i in range(remaining_moves):
                max_pair = max(max_pair, arr[i] + arr[i + 1])
            
            current_score += max_pair * left_moves
            
            score_high = max(score_high, current_score)
        
        results.append(score_high)
    
    return results

def main():
    t = int(input().strip())
    m = []
    for _ in range(t):
        n, k, z = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        m.append((n, k, z, arr))
    for result in score_high(m):
        print(result)

if __name__ == "__main__":
    main()
