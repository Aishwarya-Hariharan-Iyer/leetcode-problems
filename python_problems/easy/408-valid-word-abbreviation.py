class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w = len(word)
        a = len(abbr)

        if a > w:
            return False

        aptr = 0
        wptr = 0

        while aptr < a:
            if wptr > w:
                return False
            if abbr[aptr].isdigit():
                count = ""
                for i in range(aptr, a):
                    if abbr[i].isdigit():
                        count += abbr[i]
                        aptr += 1
                    else:
                        break
                if count:
                    if count[0] == "0":
                        return False
                    wptr += int(count)
            else:
                if wptr < w and word[wptr] != abbr[aptr]:
                    return False
                aptr += 1
                wptr += 1
                if wptr > w:
                    return False

        return wptr == w
