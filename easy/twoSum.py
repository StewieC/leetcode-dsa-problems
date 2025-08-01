class Solution:
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)):
                if nums [j] == target - nums[i]:
                    return [i, j]
                
        return []
    
solution = Solution()
test = [2, 7, 11, 15]
result = solution.twoSum(test, 9)
print(result)  # Expected output: [0, 1]
        