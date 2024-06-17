N , A = map(int, input().split())
time = list(map(int, input().split()))
dict_time = {time[i]: -1 for i in range(N)} ##キーtime[i]、値 チケット購入時間
now = 0
i = 0

for i in range(N):
    #チケット売り場にいるとき
    if(now > time[i]):
        now += A
        dict_time[time[i]] = now
    #いないとき
    else:
        #客が到着するまで待つ
        now = time[i]
        #チケット買う
        now += A
        dict_time[time[i]] = now

for i in range(N):
    print(dict_time[time[i]])