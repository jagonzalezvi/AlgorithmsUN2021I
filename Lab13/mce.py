 # Uses python3
import sys

def get_change(amount):

        coins = [1,3,4]
        
        dp = [amount + 1] * (amount + 1)


        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] > amount else dp[amount]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))