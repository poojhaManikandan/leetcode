class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        dp = [[[-1 for _ in range(2)] for _ in range(n + 1)] for _ in range(n)]
        
        def f(i, m, turn):
            if i == n:
                return 0
            if dp[i][m][turn] != -1:
                return dp[i][m][turn]
            
            if turn == 1:
                alice = 0
                total_sum = 0
                for ind in range(i, i + 2 * m):
                    if ind == n:
                        break
                    total_sum += piles[ind]
                    x = ind - i + 1
                    alice = max(alice, total_sum + f(ind + 1, max(x, m), 0))
            else:
                alice = float('inf')
                for ind in range(i, i + 2 * m):
                    if ind == n:
                        break
                    x = ind - i + 1
                    alice = min(alice, f(ind + 1, max(x, m), 1))
            
            dp[i][m][turn] = alice
            return alice
            
        return f(0, 1, 1)