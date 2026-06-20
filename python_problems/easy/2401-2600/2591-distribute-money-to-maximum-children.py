class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money = money - children #give everyone a dollar
        if money < 0:
            return -1 #Not everyone could receive a dollar
        
        count = 0
        while money >= 7 and children > 0:
            money -= 7
            count += 1
            children -= 1 #keep trying to get everyone to have 8 dollars

        if (children == 1 and money == 3) or (money > 0 and children == 0): #one child left and 4 dollars left OR more money than kids with 8 dollars
            count -= 1 #have to find way to redistribute for min. 1

        return count




        