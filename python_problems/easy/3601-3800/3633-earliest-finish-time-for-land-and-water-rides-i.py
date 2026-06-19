class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_time = float('inf')

        #Start with land
        for i in range(len(landStartTime)):
            landEnd = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                diff = waterStartTime[j] - landEnd
                waterEnd = landEnd + (diff if diff > 0 else 0) + waterDuration[j]
                min_time = min(min_time, waterEnd)

        #Start with water
        for i in range(len(waterStartTime)):
            waterEnd = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                diff = landStartTime[j] - waterEnd
                landEnd = waterEnd + (diff if diff > 0 else 0) + landDuration[j]
                min_time = min(min_time, landEnd)

        return min_time
      
        
