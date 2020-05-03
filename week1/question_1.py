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
        l = 0
        r = n
        
        mid = n/2

        while l <= r: 

            mid = l + (r - l) // 2; 

            # Check if x is present at mid 
            if isBadVersion(mid) and not isBadVersion(mid-1): 
                return mid
            
            # If isBadVersion(mid) is false, ignore left half 
            elif isBadVersion(mid) == False: 
                l = mid + 1

            # If isBadVersion(mid) is false, ignore right half
            else: 
                r = mid - 1
                
        return -1
