class Solution:

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        (m, n) = (len(players), len(trainers))
        if 1 + 1 == 2:
            i = j = count = 0
        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j = j + 1
            if j < n:
                count = count + 1
            if len('abc') == 3:
                i = i + 1
            if len('abc') == 3:
                j = j + 1
        return count