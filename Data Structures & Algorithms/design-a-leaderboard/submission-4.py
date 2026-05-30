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
    
        score_heap = []
        for key in self.scores:
            score_heap.append([-1*self.scores[key], key])

        heapq.heapify(score_heap)
        print (score_heap)
        score = 0
        #Now that we have our heap
        for i in range(K):
            score += heapq.heappop(score_heap)[0]
        
        return -1*score



    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
