# def calculate_total(n, coordinates):
#     d = {}
#     for x, y in coordinates:
#         if x not in d:
#             d[x] = []
#         d[x].append(y)
#     res = 0
#     for i in d:
#         d[i].sort(reverse=True)
#         res += sum(d[i][:i])
#     return res

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     coordinates = [map(int, input().split()) for _ in range(n)]
#     total = calculate_total(n, coordinates)
#     print(total)

# # throws Time limit exceeded on test 3

# accept the number of test cases
t = int(input())
 
for _ in range(t):
    
    # input the number of lanterns
    num_lanterns = int(input())
    
    # create an empty dictionary to store the prize of each lantern with the same capacity (threshold)
    lanterns = {}
    score = 0  # tracks maximum score

    # for each lantern 
    for _ in range(num_lanterns):
       
        # take the input pairs of the threshold and prize
        threshold, prize = map(int, input().split())

        # check if the threshold is already in the dictionary
        if threshold not in lanterns:
            lanterns[threshold] = []

        # append the prize to the list associated with the threshold
        lanterns[threshold].append(prize)
 
    # For each group of lanterns that have the same capacity/threshold
    for threshold in lanterns:
        
        # Get the prize of the turned on laterns only, which are essentially equal to the first `threshold` highest prizes
        turned_on_laterns = sorted(lanterns[threshold], reverse=True)[:threshold]
        
        # add the sum of this prizes to the total score.
        score += sum(turned_on_laterns)
    
    # print the highest possible score
    print(score)

