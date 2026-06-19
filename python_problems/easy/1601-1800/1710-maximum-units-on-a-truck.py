class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        units = 0
        boxes = 0
        n = len(boxTypes)
        for i in range(n):
            if boxes + boxTypes[i][0] <= truckSize:
                units += boxTypes[i][0] * boxTypes[i][1]
                boxes += boxTypes[i][0]
            else:
                rem_cap = truckSize - boxes
                units += rem_cap * boxTypes[i][1]
                boxes += rem_cap
        return units


        