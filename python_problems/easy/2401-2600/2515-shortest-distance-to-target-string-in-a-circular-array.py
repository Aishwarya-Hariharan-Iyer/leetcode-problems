class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)

        if words[startIndex] == target:
            return 0
        
        steps1 = 0
        foundWord = False
        for i in range(n):
            if words[(startIndex + i) % n] == target:
                foundWord = True
                break
            else:
                steps1 += 1

        if not foundWord:
            return -1

        steps2 = 0
        for i in range(n):
            if words[(startIndex - i + n) % n] == target:
                break
            else:
                steps2 += 1

        return min(steps1, steps2)



        