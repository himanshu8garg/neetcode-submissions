class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## LETS BUILD ADJ MAP
        adj = {}
        tickets.sort()
        for src, dst in tickets:
            adj[src] = []
        for src, dst in tickets:
            adj[src].append(dst)
        ## SINCE THERE IS A GUARANTEE OF A FLIGHT PATH, we wont check for cycles 
        res = ["JFK"]
        visited = set()
        def dfs(src):

            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            temp=[]
            for dest in adj[src]:
                temp.append(dest)
            for i,v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                else:
                    adj[src].insert(i,v)
                    res.pop()
            return False
        dfs("JFK")
        return res
