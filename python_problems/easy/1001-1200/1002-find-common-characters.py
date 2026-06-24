class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        common_chars = set(words[0])

        for word in words:
            common_chars = common_chars & set(word)
        
        l = []

        for c in common_chars:
            ls = min(map(lambda x: x.count(c), words))
            for i in range(ls):
                l.append(c)

        return l
            



        