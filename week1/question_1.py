# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right: 

            mid = left + (right - left) // 2; 

            # Check if x is present at mid 
            if isBadVersion(mid) and not isBadVersion(mid-1): 
                return mid
            
            # If isBadVersion(mid) is false, ignore left half 
            elif isBadVersion(mid) == False: 
                left = mid + 1

            # If isBadVersion(mid) is false, ignore right half
            else: 
                right = mid - 1
                
        return -1
