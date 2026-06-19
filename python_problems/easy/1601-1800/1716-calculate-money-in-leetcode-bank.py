class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0

        #put for first monday already
        sum_amt = 1 
        day_count = 1
        last_monday_amount = 1
        curr_amt = 1

        while day_count < n:
            print(day_count)
            if day_count % 7 == 0:
                # Monday
                curr_amt = last_monday_amount + 1
                last_monday_amount = curr_amt
                sum_amt += curr_amt
                day_count += 1
            else:
                # Not Monday
                curr_amt += 1
                sum_amt += curr_amt
                day_count += 1

        return sum_amt
        