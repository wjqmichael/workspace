class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0

        lh = [0] # lh[i] saves the max profit from prices[0] to prices[i] (incl)
        min_p = prices[0]
        for p in prices[1:]:
            lh.append(max(lh[-1], p - min_p))
            min_p = min(p, min_p)

        rh = [0] # rh[i] saves the max profit from prices[i] to the last price (incl)
        max_p = prices[-1]
        for p in reversed(prices[0:-1]):
            rh.insert(0, max(rh[0], max_p - p))
            max_p = max(max_p, p)

        #define seperator to be included in the left half
        rt = 0
        for sep in xrange(1, len(prices)):
            left = lh[sep]
            right = rh[sep + 1] if sep != len(prices) - 1 else 0
            result = left + right
            if result > rt:
                rt = result
        return rt