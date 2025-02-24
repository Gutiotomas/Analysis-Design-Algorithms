def defect(dna):
    inv_count = 0
    length = len(dna)
    for i in range(length):
        for j in range(i + 1, length):
            if dna[i] > dna[j]:
                inv_count += 1
    return inv_count

def top(n, m, sequences):
    individuals = []
    for seq in sequences:
        inv_count = defect(seq)
        individuals.append((inv_count, seq))
    individuals.sort(key=lambda x: (x[0], x[1]))
    for i in range(m):
        print(individuals[i][1])

n, m = map(int, input().split())
sequences = [input().strip() for _ in range(n)]
top(n, m, sequences)