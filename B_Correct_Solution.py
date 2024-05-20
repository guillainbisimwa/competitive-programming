number = sorted(list(input()))
bobs_answer = list(input())

zeros = []
answer = []
i = 0

while i < len(number) and number[i] == "0":
    zeros.append(number[i])
    i+=1
    
if i < len(number):
    answer.append(number[i])
i+=1
answer.extend(zeros)

while i < len(number):
    answer.append(number[i])
    i+=1
    
print("OK" if answer == bobs_answer else "WRONG_ANSWER")
