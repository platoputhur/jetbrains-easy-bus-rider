import itertools

for i in range(1, 4):
    for flowers in itertools.combinations(flower_names, i):
        print(flowers)
