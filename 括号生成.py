class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.pg(0,0,n,"")
        return self.result
    def pg(self,left:int,right:int,n:int,string:str):
        if left == n and right==n:
            self.result.append(string)
        if left < n:
            self.pg(left+1,right,n,string+"(")
        if left>right and right<n:
            self.pg(left,right+1,n,string+")")