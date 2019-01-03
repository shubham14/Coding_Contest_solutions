class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits)<1: return []
        dic={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        length=len(digits)
        res=[]
        self.getString(res,'',length,0,digits,dic)
        return res
 
    def getString(self,res,string,length,num,digits,dic):
        if num==length:
            res.append(string)
            return
        for letter in dic[digits[num]]:
            self.getString(res,string+letter,length,num+1,digits,dic)
 
test=Solution()
print(test.letterCombinations("23"))