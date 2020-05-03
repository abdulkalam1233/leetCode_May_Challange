#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

#Note:
#You may assume that both strings contain only lowercase letters.

#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true

# type 1 
# ----------------------------------------------------------------
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
#-----------------------------------------------------------------
# type 2 
# ----------------------------------------------------------------
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for i in ransomNote:
            if ransomNote[i[ > magazine[i]:
                return False
        return True
#-------------------------------------------------------------------

# type 3
# -----------------------------------------------------------------
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote)>len(magazine)):
            return False;
        if(len(ransomNote) == 0):
            return True
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for i in ransomNote:
            if ransomNote[i] > magazine[i]:
                return False
        return True
# -------------------------------------------------------------------
