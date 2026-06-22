class LogSystem:

    def __init__(self):
        self.logs = dict() #id -> timestamp

    def put(self, id: int, timestamp: str) -> None:
        self.logs[id] = timestamp


    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        ids = []
        for idx in self.logs.keys():
            timestamp = self.logs[idx]
            match granularity:
                case "Year":
                    if start[:4] <= timestamp[:4] and timestamp[:4] <= end[:4]:
                        ids += [idx]
                case "Month":
                    if start[:7] <= timestamp[:7] and timestamp[:7] <= end[:7]:
                        ids += [idx]
                case "Day":
                    if start[:10] <= timestamp[:10] and timestamp[:10] <= end[:10]:
                        ids += [idx]
                case "Hour":
                    if start[:13] <= timestamp[:13] and timestamp[:13] <= end[:13]:
                        ids += [idx]
                case "Minute":
                    if start[:16] <= timestamp[:16] and timestamp[:16] <= end[:16]:
                        ids += [idx]
                case "Second":
                    if start[:19] <= timestamp[:19] and timestamp[:19] <= end[:19]:
                        ids += [idx]
        
        return ids


        

        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)