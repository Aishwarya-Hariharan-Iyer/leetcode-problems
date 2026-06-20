class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        rem = n

        l = len(flowerbed)

        for i in range(0, l):
            
            if rem == 0: #all done
                return True

            if flowerbed[i] == 1: #occupied
                continue
            
            if i-1 >= 0 and flowerbed[i-1] == 1: #valid prev pos and adjacent
                continue

            if i < l-1 and flowerbed[i+1] == 1: #valid next pos and adjacent
                continue
            
            flowerbed[i] = 1
            rem -= 1


        return rem == 0