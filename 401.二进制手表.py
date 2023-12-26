#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res =[]
        
    def readBinaryWatch(self, turnedOn: int):
        h = [0,1,2,4,8]
        m = [0,1,2,4,8,16,32]
        for i in range(turnedOn+1):
            hn = i
            mn = turnedOn-i
            if hn>len(h) or mn>len(m):
                continue
            res = []
            self.select(0,h,[],hn)
            print(self.res,)
    
    def huisu(self,index,l,k,lenth):
        def sldelect(self,index,l,k,lenth):
            if len(k)==lenth:
                self.res.append(k.copy())
                return
            for i in range(index+1,len(l)):
                k.append(l[i])
                index+=1
                self.select(index,l,k,lenth)
                k.remove(l[i])
                # self.res.append(k)

# @lc code=end

if __name__=="__main__":
    s = Solution()
    s.readBinaryWatch(7)
    # s.pp()