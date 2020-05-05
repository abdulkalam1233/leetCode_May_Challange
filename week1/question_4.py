class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2::];
        result = ''
        for i in binary:
            if(i == '1'):
                result += '0'
            else:
                result += '1'
        return int(result,2)
# ----------------------------------------------
# type 2
class Solution:
    def findComplement(self, num: int) -> int:
        digits  = math.ceil(math.log2(num + 1))
        return pow(2,digits)-1-num
