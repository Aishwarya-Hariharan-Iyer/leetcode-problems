class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words[0])
        
        def find_str_arr(word):
            arr = [0]*n
            for i in range(n-1):
                arr[i] = ord(word[i+1]) - ord(word[i])
            return str(arr)

        arr1 = ""
        word1 = ""
        arr2 = ""
        word2 = ""
        count1 = 0
        count2 = 0

        searchWord1 = False

        for word in words:
            arr = find_str_arr(word)
            print(word)
            print(arr)
            if arr1 == "" and arr != arr2:
                print("hi1")
                arr1 = arr
                count1 += 1
                word1 = word
            elif arr2 == "" and arr != arr1:
                print("hi2")
                arr2 = arr
                count2 += 1
                word2 = word
            else:
                if arr == arr1:
                    searchWord1 = False
                else:
                    searchWord1 = True
        
        return word1 if searchWord1 else word2

        
