words = input("Input: ").split()
seen = {}
for i, word in enumerate(words):
    if word not in seen:
        seen[word] = 1
    else:
        seen[word] += 1
print(" ".join(sorted(seen.keys())))
