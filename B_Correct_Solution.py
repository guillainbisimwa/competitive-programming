# def bobAndAlice(bob, alice):
#     """
#     -------------input------------
#     bob = 3310
#     alice = 1033
#     """
# bob = int(input())
# alice = int(input())
# print(bobAndAlice(bob, alice))
number = list(input())
boob_answer = list(input())

zeros = []
smallest = ""
answer = []
i = 0

while i < len(number) and number == "0":
    answer.append(number[i])
    i += 1
if i < len(number):
    answer.append(number[i])

i += 1
answer.extend(zeros)

while i < len(number):
    answer.append(number[i])
    i += 1
print("OK" if answer == boob_answer else "WRONG_ANSWER")

