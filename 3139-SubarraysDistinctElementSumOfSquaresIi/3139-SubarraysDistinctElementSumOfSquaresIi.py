# Last updated: 11/11/2026, 4:43:59 pm
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def update(node, start, end, l, r, val):
            # Resolve pending lazy updates
            if lazy[node]:
                lz = lazy[node]
                lazy[node] = 0
                length = end - start + 1
                tree_sq[node] = (tree_sq[node] + 2 * lz * tree_sum[node] + lz * lz * length) % MOD
                tree_sum[node] = (tree_sum[node] + lz * length) % MOD
                if start != end:
                    lazy[2 * node] = (lazy[2 * node] + lz) % MOD
                    lazy[2 * node + 1] = (lazy[2 * node + 1] + lz) % MOD
                    
            if start > end or start > r or end < l:
                return
                
            # Current segment is fully within update range
            if start >= l and end <= r:
                length = end - start + 1
                tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
                tree_sum[node] = (tree_sum[node] + val * length) % MOD
                if start != end:
                    lazy[2 * node] = (lazy[2 * node] + val) % MOD
                    lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % MOD
                return
                
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        ans = 0
        last_seen = {}
        
        for i, num in enumerate(nums):
            prev = last_seen.get(num, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + tree_sq[1]) % MOD
            last_seen[num] = i
            
        return ans