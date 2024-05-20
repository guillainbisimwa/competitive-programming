# def bobAndAlice(bob, alice):
#     """
#     -------------input------------
#     bob = 3310
#     alice = 1033
#     """
# bob = int(input())
# alice = int(input())
# print(bobAndAlice(bob, alice))

def eatingCandies():
    num_candies = int(input())

    weights = list(map(int, input().split()))
    left = 0

    right = num_candies - 1

    alice_weight = weights[0]

    bob_weight = weights [num_candies - 1]

    max_candies = 0

    while left < right:

        if alice_weight == bob_weight:

            max_candies = max(max_candies, left + 1 + num_candies - right)

        if alice_weight <= bob_weight: #, 
            left += 1

            alice_weight += weights [left]

        elif bob_weight < alice_weight:

            right -= 1 
            bob_weight += weights [right]

    print(max_candies)

num_test_cases = int(input())

for _ in range(num_test_cases):

    eatingCandies()