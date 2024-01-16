n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

stack = []
answer = []
answer_num = []
current = 0

for i in range(1, n + 1):
    stack.append(i)
    answer.append('+')
    if li[current] == i:
        while stack and current < len(li) and li[current] == stack[-1]:
            answer_num.append(stack.pop())
            current += 1
            answer.append('-')

while stack:
    answer_num.append(stack.pop())
    answer.append('-')

if answer_num != li:
    print("NO")
else:
    for i in answer:
        print(i)

