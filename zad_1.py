class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1

        while self.size < self.n:
            self.size <<= 1

        self.tree = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update_val(self, index, value):
        pos = self.size + index
        self.tree[pos] = value

        pos >>= 1
        while pos >= 1:
            new_val = self.tree[2 * pos] + self.tree[2 * pos + 1]
            if self.tree[pos] == new_val:
                break
            self.tree[pos] = new_val
            pos >>= 1

    def get_sum(self, l, r):
        res = 0
        l += self.size
        r += self.size

        while l <= r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res


input_data = open('sum.in').read().split()
ptr = 0
N, K = int(input_data[ptr]), int(input_data[ptr + 1])
ptr += 2

st = SegmentTree([0] * N)
output = []

for _ in range(K):
    cmd = input_data[ptr]

    if cmd == 'A':
        i = int(input_data[ptr + 1]) - 1
        x = int(input_data[ptr + 2])
        ptr += 3
        st.update_val(i, x)
        
    elif cmd == 'Q':
        l = int(input_data[ptr + 1]) - 1
        r = int(input_data[ptr + 2]) - 1
        ptr += 3
        output.append(str(st.get_sum(l, r)))

with open('sum.out', 'w') as f:
    f.write('\n'.join(output))