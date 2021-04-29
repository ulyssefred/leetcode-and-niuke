class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        candidates.sort()
        def dfs(target, path, idx):
            if idx>=len(candidates):
                return
            if target<0:
                return
            if target == 0:
                res.append(path)
                return
            dfs(target,path,idx+1)
            dfs(target-candidates[idx],path+[candidates[idx]],idx)
        dfs(target,[],0)
        return res