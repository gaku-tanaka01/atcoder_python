from itertools import combinations

N, M = map(int, input().split())
stores = [None] * N
for i in range(N):
    stores[i] = input()

def generate_all_combinations(n):
    elements = list(range(n))  # 0からn-1までの数のリストを作成
    all_combinations = []
    for r in range(1, n + 1):  # 1個からn個までの組み合わせを生成
        all_combinations.extend(combinations(elements, r))
    return all_combinations


selected_stores_list = generate_all_combinations(N)


def check(selected_stores):
    want_buy = [False] * len(stores[0])  # 商品の購入希望を初期化
    for store_index in selected_stores:
        for i, c in enumerate(stores[store_index]):
            if c == 'o':
                want_buy[i] = True

    return want_buy.count(True) == M


result = []
for selected_stores in selected_stores_list:
    if check(selected_stores):
        result.append(len(selected_stores))

print(min(result))
        
            

