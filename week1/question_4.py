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
                
