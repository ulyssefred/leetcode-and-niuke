class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        flag = 1
        i = 0
        while str[i] == " ":
            i += 1
            if i == len(str):
                return 0
        if str[i] == "-":
            flag = -1
            i +=1
        elif str[i] == "+":
            flag = 1
            i +=1
        res = 0
        minv = -2 ** 31
        maxv = 2 ** 31 - 1
        bndry = 2 ** 31 // 10
        for i in str[i:]:
            if i == " ":
                break
            if not "0"<= i<="9":
                break
            if res>bndry or res==bndry and i>"7":
                return minv if flag == -1 else maxv
            res = res * 10 + ord(i) - ord('0')
        return flag*res