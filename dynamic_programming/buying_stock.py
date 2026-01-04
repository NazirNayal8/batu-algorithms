



def maxProfit(prices):
    low = prices[0]
    high = -1
    for i in range(len(prices)):
        if prices[i] < low:
            low = prices[i]
        if prices[i]-low > high:
            high = prices[i]-low
    return high

# [2, 10, 1, 5]




if __name__ == "__main__":
    # Example usage:
    prices = [7,6,4,3,1] # [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))  # Output: 5