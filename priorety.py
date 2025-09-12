def SiftDown(i):
    left = 2 * i + 1
    right = 2 * i + 2
    max_elem = left
    if left > heap_size - 1:
        return i
    if (right <= (heap_size - 1)) and (heap[right] > heap[left]):
        max_elem = right
    if heap[i] >= heap[max_elem]:
        return i
    else:
        heap[i], heap[max_elem] = heap[max_elem], heap[i]
    return SiftDown(max_elem)



def SiftUp(i):
    if i == 0:
        return 0
    parent = (i - 1) // 2
    if heap[i] > heap[parent]:
        heap[i], heap[parent] = heap[parent], heap[i]
    else:
        return i
    return SiftUp(parent)


heap_size = 0
max_size, m = map(int, input().split())
heap = [0 for _ in range(max_size)]
for i in range(m):
    a, *b = map(int, input().split())
    if a == 1:
        if heap_size > 1:
            ans_val = heap[0]
            heap_size -= 1
            heap[0] = heap[heap_size]
            ans_ind = SiftDown(0)
            print(ans_ind + 1, ans_val)
        elif heap_size == 1:
            heap_size -= 1
            print(0, heap[0])
        else:
            print(-1)
    else:
        b = b[0]
        if heap_size == max_size:
            print(-1)
        else:
            heap_size += 1
            heap[heap_size - 1] = b
            ans_ind = SiftUp(heap_size - 1)
            print(ans_ind + 1)
for i in range(heap_size):
    print(heap[i], end=' ')