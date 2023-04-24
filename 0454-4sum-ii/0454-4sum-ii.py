class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}
        ans = 0
        sA = len(A)
        sB = len(B)
        sC = len(C)
        sD = len(D)
        
        for i in range(0,sA):
            x = A[i]
            for j in range(0,sB):
                y = B[j]
                
                if x+y not in m:
                    m[x+y] = 0
                    
                m[x+y] += 1
                
        for i in range(0,sC):
            x = C[i]
            for j in range(0,sD):
                y = D[j]
                target = -(x+y)
                if target in m:
                    ans += m[target]
        
        return ans