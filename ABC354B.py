N = int(input())

class User:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

users = []
for i in range(N):
    name, rate = input().split()
    users.append(User(name, int(rate)))

for i in range(N - 1):
    for j in range(N - 1):
        
        for k, c in enumerate(users[i].name):
            same = True ## 文字列がkまで同じフラグ
            if ord(c) > ord(users[j].name[k]):
                print("users[i] = {}  users[j] = {} ord(c) = {} k = {}".format(users[i].name, users[j].name, ord(c), users[j].name[k]))
                users[i], users[j] = users[j], users[i]
                break
            elif ord(c) != ord(users[j].name[k]):
                same = False
            if k == len(users[i].name) - 1:
                if same:
                    if len(users[i].name) > len(users[j].name):
                        users[i], users[j] = users[j], users[i]

            
            
            


for i in range(N):
    print(users[i].name, users[i].rate)