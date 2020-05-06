class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        length = len(nums)
        for i in numCount:
            if(numCount[i] > length/2):
                return i
        return -1
        
# using Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
