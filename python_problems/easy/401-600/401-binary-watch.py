class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = defaultdict(list)
        minutes = defaultdict(list)
        
        for h in range(12):
            hours[h.bit_count()].append(h)
        for m in range(60):
            minutes[m.bit_count()].append(m)

        valid_times = []
        for hrs in range(min(3, turnedOn) + 1):
            mins = turnedOn - hrs
            if mins > 5:
                continue
            all_h = hours[hrs]
            all_m = minutes[mins]

            for h in all_h:
                for m in all_m:
                    s = str(h) + ":" + (str(m) if m > 9 else "0" + str(m))
                    valid_times.append(s)
            
        return valid_times
            
        

        