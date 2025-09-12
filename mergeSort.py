class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        current_size = 1
        n = len(nums)

        while current_size < n:
            left = 0
            while left < n:
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)

                merged = []
                i, j = left, mid + 1

                while i <= mid and j <= right:
                    if nums[i] <= nums[j]:
                        merged.append(nums[i])

                        i += 1
                    else:
                        merged.append(nums[j])
                        j += 1

                while i <= mid:
                    merged.append(nums[i])
                    i += 1

                while j <= right:
                    merged.append(nums[j])
                    j += 1

                for index in range(left, right + 1):
                    nums[index] = merged[index - left]

                left += 2 * current_size

            current_size *= 2

        return nums
