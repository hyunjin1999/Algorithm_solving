import math

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    first_num = abs(li[0] - (li[1] * 2 - li[2]))
    sec_num = abs(li[1] - ((li[0] + li[2]) / 2))
    third_num = abs(li[2] - (li[1] * 2 - li[0]))
    ans = min(first_num, sec_num, third_num)
    print("#{} {:.1f}".format(test_case, ans))
