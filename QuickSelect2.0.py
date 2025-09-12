class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            if self.IsSorted(nums, left, right):
                return nums[right - k + 1]
            pivot_idx = self.medianOfMedians(nums, left, right)
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            p_index = self.partition(nums, left, right)
            if right - k + 1 < p_index:
                k -= (right - p_index + 1)
                right = p_index - 1
            elif right - k + 1 > p_index:
                left = p_index + 1
            else:
                return nums[p_index]

    def partition(self, nums: List[int], l: int, r: int) -> int:
        x = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] < x:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def IsSorted(self, arr: List[int], l: int, r: int) -> bool:
        for i in range(l + 1, r + 1):
            if arr[i] < arr[i - 1]:
                return False
        return True

    def insertionSort(self, nums: List[int], l: int, r: int) -> None:
        for i in range(l + 1, r + 1):
            temp = nums[i]
            j = i - 1
            while j >= l and temp < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

    def medianOfMedians(self, nums: List[int], left: int, right: int) -> int:
        if right - left + 1 <= 5:
            self.insertionSort(nums, left, right)
            return left + (right - left) // 2

        num_groups = (right - left + 4) // 5
        medians_end = left + num_groups - 1

        for i in range(left, right + 1, 5):
            group_right = min(i + 4, right)
            self.insertionSort(nums, i, group_right)
            median_idx = i + (group_right - i) // 2
            nums[left + (i - left) // 5], nums[median_idx] = nums[median_idx], nums[left + (i - left) // 5]


        return self.medianOfMedians(nums, left, medians_end)