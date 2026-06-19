class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        answer = []
        for i in range(l):
            price = prices[i]
            if i < l-1:
                for j in range(i+1, l):
                    if prices[j] <= price:
                        price -= prices[j]
                        break
            answer += [price]
        return answer
