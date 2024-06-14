S = input()
lower_count = 0
for c in S:
    if c.islower():
        lower_count += 1

result = ""
if lower_count > len(S) / 2:
    for c in S:
        result = result + c.lower()
else:
    for c in S:
        result = result + c.upper()
print(result)
