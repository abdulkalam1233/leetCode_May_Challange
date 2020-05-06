class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        length = len(nums)
        for i in numCount:
            if(numCount[i] > length/2):
                return i
        return -1
        
