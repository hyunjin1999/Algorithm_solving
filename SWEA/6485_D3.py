T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bus_stop = [0 for i in range(5001)]  # 정류장
    ans = '#' + str(test_case) + ' '
    N = int(input())
    for i in range(N):
        A1, B1 = map(int, input().split())
        for j in range(A1, B1 + 1):
            bus_stop[j] += 1
    P = int(input())
    for _ in range(P):
        n = int(input())
        ans += str(bus_stop[n]) + ' '

    print(ans[:-1])