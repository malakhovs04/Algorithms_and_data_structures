class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k < n // 2:
            new_ind = 0
            for i in range(n - k, n):
                temp_element = nums[i]
                for j in range(new_ind, i + 1):
                    temp = nums[j]
                    nums[j] = temp_element
                    temp_element = temp
                new_ind += 1
        else:
            new_ind = n - 1
            for i in range(n - k - 1, -1, -1):
                temp_element = nums[i]
                for j in range(new_ind, i - 1, -1):
                    temp = nums[j]
                    nums[j] = temp_element
                    temp_element = temp
                new_ind -= 1
        return nums