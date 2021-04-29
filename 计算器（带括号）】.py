class Solution:
    def calculate(self, s: str) -> int:
        self.l = list(s)
        return self.Calculates(self.l)

    def Calculates(self, l):
        num = 0
        sign = "+"
        res = []
        while l:
            char = l.pop(0)
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.Calculates(l)
            if (not char.isdigit() and char != " ") or not l:
                if sign == "+":
                    res.append(num)
                if sign == "-":
                    res.append(-num)
                if sign == "*":
                    res.append(res.pop() * num)
                if sign == "/":
                    res.append((res.pop()//num))
                num = 0
                sign = char
            if char == ")":
                break
        return sum(res)

arr = "1+2"
test = Solution()
print(test.calculate(arr))
