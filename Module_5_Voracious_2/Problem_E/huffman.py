import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq

def huffman_encoding(char_freqs):
    heap = [Node(char, freq) for char, freq in char_freqs]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(left.char + right.char, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_codes(root, prefix='', codes=None):
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.left is None and root.right is None:
        codes[root.char] = prefix

    generate_codes(root.left, prefix + '0', codes)
    generate_codes(root.right, prefix + '1', codes)

    return codes

def in_order_traversal(root, codes):
    result = []
    
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        if node.char and len(node.char) == 1:
            result.append((node.char, codes[node.char]))
        traverse(node.right)

    traverse(root)
    return result

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    char_freqs = []
    
    for _ in range(N):
        line = input().split()
        char, freq = line[0], int(line[1])
        char_freqs.append((char, freq))

    char_freqs.sort()

    root = huffman_encoding(char_freqs)

    codes = generate_codes(root)

    result = in_order_traversal(root, codes)

    print(f"caso {case}:")
    for char, code in result:
        print(f"{char} {code}")
    print()