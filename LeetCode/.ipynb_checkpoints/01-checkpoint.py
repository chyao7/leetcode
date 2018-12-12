class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s.strip(' ').split(' ')
        print(x)
        str_list = [i for i in x if x != '']
        print(str_list)
        if len(str_list) != 0:
            if str_list[-1].isalpha():
                return len(str_list[-1])
            else:
                return 0
        else:
            return 0



if __name__ == '__main__':
    c = Solution()
    str = str(input('请输入字符串'))

    len = c.lengthOfLastWord(str)
    print(len)

