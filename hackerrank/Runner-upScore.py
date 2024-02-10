if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    new_arr = list(arr)

    new_arr.sort(reverse=True)


    max_score = max(new_arr)
    runner_up_score = max(s for s in new_arr if s < max_score)

    print(runner_up_score)