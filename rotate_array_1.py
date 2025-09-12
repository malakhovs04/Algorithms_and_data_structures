def reverse (l, r, nums):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reverse(0, len(nums) - k - 1, nums)
        reverse(len(nums) - k, len(nums) - 1, nums)
        reverse(0, len(nums) - 1, nums)
        return nums

