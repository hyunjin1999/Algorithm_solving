import math

T = int(input())
li = []
ans = ''
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li.append(int(input()))
for idx,i in enumerate(li):
    for j in range(1, 16):
        if math.sqrt(i*j) / j == 1.0:
            ans = "#" + str(idx+1) + ' ' + str(j)
            break
    print(ans)

