class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) == 0:
            return True
        
        if len(moves) % 2 == 1:
            return False

        original_pos = [0, 0]
        tracks = dict({"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]})
        
        for move in moves:
            to_move = tracks[move]
            original_pos[0] += to_move[0]
            original_pos[1] += to_move[1]

        return original_pos == [0, 0]
