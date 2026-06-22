class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        words = sentence.split(" ")
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            for j in range(i+1):
                word += "a"
            words[i] = word
        return " ".join(words)
        