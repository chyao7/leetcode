#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str):
        self.res = []
        def solve(st,index):
            for i in range(index,len(st)):
                tmps = st[:i]+"."+st[i:]

                stl = tmps.split(".")
                index = i+2    
                if len(stl)==4:
                        if 0<=int(stl[-1])<=255 and 0<=int(stl[-2])<=255  and len(str(int(stl[-2])))==len(stl[-2]) and len(str(int(stl[-1])))==len(stl[-1]):
                            self.res.append(tmps)
                        elif not 0<=int(stl[-2])<=255 or len(str(int(stl[-2])))!=len(stl[-2]):
                            return
                elif len(stl)<4 and len(str(int(stl[-2])))==len(stl[-2]) and 0<=int(stl[-2])<=255:
                     
                    solve(tmps,index)
                tmps = st
        solve(s,1)
        return self.res
            

# @lc code=end

if __name__=="__main__":
    s = Solution()
    s.restoreIpAddresses("101023")
    #["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
