#type 1
# -------------------------------------------------------
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        obj = {}
        for i in J:
            obj[i] = 0
        for i in S:
            if(i in obj):
                obj[i]+=1
        
        return sum(obj.values())
        
# ---------------------------------------------------------       

# type 2
# slow compare to above solution

from Collection import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        S = Counter(S)
        result = 0
        for i in J:
            result+=S[i]
        return result
        
