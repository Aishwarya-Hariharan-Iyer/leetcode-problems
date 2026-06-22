from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.changes = defaultdict(list) # index -> (snap_id, value)
        

    def set(self, index: int, val: int) -> None:

        changes_so_far = self.changes[index]
        l = len(changes_so_far)

        if l > 0:
            #if snapshot id changes or not but value is same, we retain old snapId
            if changes_so_far[-1][1] == val:    
                pass
            # if latest snapshot id is same (no snap called between sets), we only update value
            elif changes_so_far[-1][0] == self.snap_id:
                changes_so_far[-1] = (self.snap_id, val)
                self.changes[index] = changes_so_far
            else:
                self.changes[index].append((self.snap_id, val))
        else:
            self.changes[index].append((self.snap_id, val))

    def snap(self) -> int:
        snap_id = self.snap_id
        self.snap_id += 1
        return snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        
        ind_changes = self.changes[index]
        l = len(ind_changes)
        
        if l == 0:
            return 0
        
        lp = 0
        rp = l-1
        
        # for i in range(l-1, -1, -1):
        #     snap_hist_id, val = ind_changes[i]
        #     if snap_hist_id <= snap_id:
        #         return val
        while lp <= rp:
            mid = lp + (rp - lp + 1)//2
            if ind_changes[mid][0] == snap_id:
                return ind_changes[mid][1]
            elif mid == l-1 and ind_changes[mid][0] < snap_id:
                return ind_changes[mid][1]
            elif mid == 0 and ind_changes[mid][0] > snap_id:
                return 0 # no change
            elif ind_changes[mid][0] < snap_id and ind_changes[mid+1][0] > snap_id:
                return ind_changes[mid][1]
            elif ind_changes[mid][0] < snap_id:
                lp = mid + 1
            else:
                rp = mid - 1
            
        
        return 0 # no changes

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = dict() # index -> curr value (0 for all index not in arr)
        self.changes = defaultdict(list) # index -> (snap_id, value)
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val # overwrite ok
        if len(self.changes[index]) > 0 and self.changes[index][-1][1] == val:
            pass
        else:
            self.changes[index].append((self.snap_id, val))

    def snap(self) -> int:
        snap_id = self.snap_id
        self.snap_id += 1
        return snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        
        ind_changes = self.changes[index]
        l = len(ind_changes)
        
        if l == 0:
            return 0
        
        for i in range(l-1, -1, -1):
            snap_hist_id, val = ind_changes[i]
            if snap_hist_id <= snap_id:
                return val
        
        return 0 # no changes

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)