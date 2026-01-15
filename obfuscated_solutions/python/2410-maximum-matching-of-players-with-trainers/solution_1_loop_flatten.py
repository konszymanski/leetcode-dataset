class Solution:

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]
        ) ->int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0
        while True:
            if not (i < m and j < n):
                break
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1
        return count
