import random


def confirm():
    colors = ["red", "blue", "white"]
    color_to_index = {"red": 0, "blue": 1, "white": 2}
    index_to_color = {0: "red", 1: "blue", 2: "white"}

    persons = ["A", "B", "C"]

    # 色をランダムにシャッフルしてから割り振る　重複あり
    assigned_colors = {person: random.choice(colors) for person in persons}

    # 予想した色を格納する辞書を作成
    guessed_colors = {person: "" for person in persons}

    # 予想A色を計算して格納
    for person in persons:
        if person == "A":
            # 事実B色と事実C色のインデックスの合計を計算
            sum_fact_colors = color_to_index[assigned_colors["B"]
                                             ] + color_to_index[assigned_colors["C"]]
            # 予想A色のインデックスを計算
            # 予想A色のインデックスを見つける
            for i in range(3):
                if (sum_fact_colors + i) % 3 == 0:
                    guessed_color_index = i
                    break
            guessed_colors["A"] = index_to_color[guessed_color_index]
        if person == "B":
            # 事実A色と事実C色のインデックスの合計を計算
            sum_fact_colors = color_to_index[assigned_colors["A"]
                                             ] + color_to_index[assigned_colors["C"]]
            # 予想B色のインデックスを計算
            for i in range(3):
                if (sum_fact_colors + i) % 3 == 1:
                    guessed_color_index = i
                    break
            guessed_colors["B"] = index_to_color[guessed_color_index]
        if person == "C":
            # 事実A色と事実B色のインデックスの合計を計算
            sum_fact_colors = color_to_index[assigned_colors["A"]
                                             ] + color_to_index[assigned_colors["B"]]
            # 予想C色のインデックスを計算
            for i in range(3):
                if (sum_fact_colors + i) % 3 == 2:
                    guessed_color_index = i
                    break
            guessed_colors["C"] = index_to_color[guessed_color_index]
    print("予想:", guessed_colors, "事実:", assigned_colors)
    for person in persons:
        if assigned_colors[person] == guessed_colors[person]:
            print(f"{person}は{guessed_colors[person]}で当たりです")
            return True

    return False


test_count = 10000
true_count = 0

for i in range(test_count):
    if confirm():
        true_count += 1
    else:
        print("no")

print(f"試行回数:{test_count} 当たりの確率:{true_count / test_count * 100}%")
