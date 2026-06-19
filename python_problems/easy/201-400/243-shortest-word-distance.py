class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        pos1 = -1
        pos2 = -1
        dist = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
            if wordsDict[i] == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1:
                dist = min(dist, abs(pos1 - pos2))
        
        return dist
