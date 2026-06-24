class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        l = len(word)

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        count = 0

        for i in range(l):
            uv = set()
            for j in range(i, l):
                if word[j] not in vowels:
                    break
                uv.add(word[j])
                if len(uv) == 5:
                    count += 1

        return count

        