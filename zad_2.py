class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1

        while self.size < self.n:
            self.size <<= 1


        self.min_tree = [float('inf')] * (2 * self.size)
        self.max_tree = [float('-inf')] * (2 * self.size)


        for i in range(self.n):
            self.min_tree[self.size + i] = data[i]
            self.max_tree[self.size + i] = data[i]


        for i in range(self.size - 1, 0, -1):
            self.min_tree[i] = min(self.min_tree[2 * i], self.min_tree[2 * i + 1])
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])

    def update_val(self, index, value):
        pos = self.size + index
        self.min_tree[pos] = value
        self.max_tree[pos] = value
        pos >>= 1

        while pos >= 1:
            new_min = min(self.min_tree[2 * pos], self.min_tree[2 * pos + 1])
            new_max = max(self.max_tree[2 * pos], self.max_tree[2 * pos + 1])


            if self.min_tree[pos] == new_min and self.max_tree[pos] == new_max:
                break

            self.min_tree[pos] = new_min
            self.max_tree[pos] = new_max
            pos >>= 1

    def get_min_max(self, l, r):
        min_res = float('inf')
        max_res = float('-inf')
        l += self.size
        r += self.size

        while l <= r:
            if l % 2 == 1:
                min_res = min(min_res, self.min_tree[l])
                max_res = max(max_res, self.max_tree[l])
                l += 1
            if r % 2 == 0:
                min_res = min(min_res, self.min_tree[r])
                max_res = max(max_res, self.max_tree[r])
                r -= 1
            l >>= 1
            r >>= 1

        return (min_res, max_res)


n = 100000
a = [0] * n
for i in range(1, n + 1):
    a[i - 1] = (i * i) % 12345 + (i * i * i) % 23456


input_data = open('rvq.in').read().split()
ptr = 0
k = int(input_data[ptr])
ptr += 1
output = []

st = SegmentTree(a)


for _ in range(k):
    x = int(input_data[ptr])
    y = int(input_data[ptr + 1])
    ptr += 2

    if x > 0:
        l, r = x - 1, y - 1
        current_min, current_max = st.get_min_max(l, r)
        output.append(str(current_max - current_min))
    else:
        index = abs(x) - 1
        st.update_val(index, y)


with open('rvq.out', 'w') as f:
    f.write('\n'.join(output))