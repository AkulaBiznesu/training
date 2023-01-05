nums = [2,7,11,15]
target =  int(9)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] == target - nums[i]:
            print([i, j])
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[j]:
                    return [i, j]

class Solution(object):
    def isPalindrome(self, x):
        if x == int(str(x)[::-1]):
            print("True")
        else:
            print("False")

p = Solution.isPalindrome(276)
print(p)