class Solution:
    def combinationSum2(self , num , target ):
        candidates = num
        if not candidates:
            return []
        res = []
        candidates.sort()
        def dfs(target, path, idx):
            if target<0:
                return
            if target == 0:
                if path not in res:
                    res.append(path)
                return
            if idx>=len(candidates):
                return
            dfs(target-candidates[idx],path+[candidates[idx]],idx+1)
            dfs(target,path,idx+1)
        dfs(target,[],0)
        return res
#2
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans
