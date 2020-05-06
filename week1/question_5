class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        for i,v in enumerate(s):
            if(s_count[v] == 1):
                return i
        return -1
