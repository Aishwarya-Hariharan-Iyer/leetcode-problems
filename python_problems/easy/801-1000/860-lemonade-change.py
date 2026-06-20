class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = dict()
        for bill in bills:
            if bill == 5:
                notes[5] = notes.get(5, 0) + 1
            elif bill == 10:
                if notes.get(5, 0) == 0:
                    return False
                notes[5] = notes.get(5) - 1
                notes[10] = notes.get(10, 0) + 1
            elif bill == 20:
                if notes.get(10, 0) > 0 and notes.get(5, 0) > 0:
                    notes[5] = notes.get(5) - 1
                    notes[10] = notes.get(10) - 1
                    notes[20] = notes.get(20, 0) + 1
                elif notes.get(5, 0) >= 3:
                    notes[5] = notes.get(5) - 3
                    notes[20] = notes.get(20, 0) + 1
                else:
                    return False
        return True