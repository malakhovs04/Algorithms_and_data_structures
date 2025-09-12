def solve():
    try:
        n = int(input())
        nodes_input = []
        for i in range(n):
            a, b = map(int, input().split())
            nodes_input.append({'key': a, 'priority': b, 'orig_idx': i + 1})

        sorted_nodes = sorted(nodes_input, key=lambda x: x['key'])
        parent = [0] * (n + 1)
        left = [0] * (n + 1)
        right = [0] * (n + 1)

        stack = []
        for i in range(n):
            current_node = sorted_nodes[i]
            current_priority = current_node['priority']
            current_orig_idx = current_node['orig_idx']
            last_popped_sorted_idx = -1

            while stack and sorted_nodes[stack[-1]]['priority'] > current_priority:
                last_popped_sorted_idx = stack.pop()

            if last_popped_sorted_idx != -1:
                popped_orig_idx = sorted_nodes[last_popped_sorted_idx]['orig_idx']
                left[current_orig_idx] = popped_orig_idx
                parent[popped_orig_idx] = current_orig_idx
            if stack:
                stack_top_orig_idx = sorted_nodes[stack[-1]]['orig_idx']
                right[stack_top_orig_idx] = current_orig_idx
                parent[current_orig_idx] = stack_top_orig_idx
            stack.append(i)
        print("YES")
        for i in range(1, n + 1):
            print(f"{parent[i]} {left[i]} {right[i]}")
    except Exception as e:
        pass


solve()
