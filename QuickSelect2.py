from typing import List

def partition(vals, l, r):
    x = vals[r]
    i = l
    for j in range(l, r):
        if vals[j] < x:
            vals[i], vals[j] = vals[j], vals[i]
            i += 1
    vals[i], vals[r] = vals[r], vals[i]
    return i


def is_sorted(arr, l, r):
    for i in range(l + 1, r + 1):
        if arr[i] < arr[i - 1]:
            return False
    return True


def insertion_sort(vals, l, r):
    for i in range(l + 1, r + 1):
        temp = vals[i]
        j = i - 1
        while j >= l and temp < vals[j]:
            vals[j + 1] = vals[j]
            j -= 1
        vals[j + 1] = temp


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            if is_sorted(nums, left, right):
                return nums[right - k + 1]

            num_len = right - left + 1
            groups_counter = (num_len + 4) // 5

            # Сортируем группы по 5 элементов и перемещаем медианы в начало массива
            for i in range(groups_counter):
                group_left = left + i * 5
                group_right = min(group_left + 4, right)
                insertion_sort(nums, group_left, group_right)
                median_idx = group_left + (group_right - group_left) // 2
                # Перемещаем медиану группы в позицию left + i
                nums[left + i], nums[median_idx] = nums[median_idx], nums[left + i]

            # Сортируем медианы (находятся в nums[left:left+groups_counter])
            insertion_sort(nums, left, left + groups_counter - 1)

            # Выбираем медиану медиан
            median_of_medians_idx = left + (groups_counter - 1) // 2

            # Перемещаем медиану медиан в конец для использования в partition
            nums[right], nums[median_of_medians_idx] = nums[median_of_medians_idx], nums[right]

            p_index = partition(nums, left, right)
            if right - k + 1 < p_index:
                k -= (right - p_index + 1)
                right = p_index - 1
            elif right - k + 1 > p_index:
                left = p_index + 1
            else:
                return nums[p_index]