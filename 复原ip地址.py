class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        segment = [0]*4
        def dfs(segmentid, segstart):
            if segmentid == 4:
                if segstart == len(s):
                    ans.append(".".join(map(str,segment)))
                return
            if segstart == len(s):
                return
            if s[segstart] == "0":
                segment[segmentid] = 0
                dfs(segmentid+1,segstart+1)
            arr = 0
            for i in range(segstart,len(s)):
                arr = arr*10 + (ord(s[i])-ord("0"))
                if 0<arr <=255:
                    segment[segmentid] = arr
                    dfs(segmentid+1,i+1)
                else:
                    break
        dfs(0,0)
        return ans