def find_minimum_swaps(test):
    swapped = False
    for i in range(len(test)):
        min_idx = i
        for j in range(i+1, len(test)):
            if test[j] < test[min_idx]:
                min_idx = j
                swapped = True
        if swapped:
            test[i], test[min_idx] = test[min_idx], test[i]
            break
    return test

def check_order(test):
    if test[0] < test[1] and test[1] < test[2]:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    test = input()
    test = [char for char in test]
    
    test = find_minimum_swaps(test)
    print(check_order(test))

