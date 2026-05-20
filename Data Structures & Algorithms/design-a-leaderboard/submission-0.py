class Leaderboard:

    def __init__(self):
        
        self.scores = {}


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
        else:
            self.scores[playerId] += score

    def top(self, K: int) -> int:
        ## TO FIND THE TOP K players we need to arrange the dict in descending order and then we can iterate over the list for 0 to k-1
        values = []
        for key in self.scores:
            values.append(self.scores[key])
        total_k = 0
        print (values)
        values.sort()
        values.sort(reverse=True)
        print (values)
        i=0
        for i in range(K):
            total_k+=values[i]
        
        return total_k


    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
