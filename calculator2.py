def SiftDown(i):
    left = 2 * i + 1
    right = 2 * i + 2
    min_elem = left
    if left > len(heap) - 1:
        return i
    if (right <= (len(heap) - 1)) and (heap[right] < heap[left]):
        min_elem = right
    if heap[i] <= heap[min_elem]:
        return i
    else:
        heap[i], heap[min_elem] = heap[min_elem], heap[i]
    return SiftDown(min_elem)



def SiftUp(i):
    if i == 0:
        return 0
    parent = (i - 1) // 2
    if heap[i] < heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
    else:
        return i
    return SiftUp(parent)


def ExtractMin():
    ans_val = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.pop(len(heap) - 1)
    SiftDown(0)
    return ans_val


def Append(val):
    heap.append(val)
    SiftUp(len(heap) - 1)


n = int(input())
elems = list(map(int, input().split()))
heap = []
for i in range(n):
    Append(elems[i])
ans = 0
while n > 1:
    min_val1 = ExtractMin()
    min_val2 = ExtractMin()
    ans += (min_val1 + min_val2) * 0.05
    Append(min_val1 + min_val2)
    n -= 1
print("{:.2f}".format(ans))