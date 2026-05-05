class Solution:
    def reorganizeString(self, s: str) -> str:
        #"aabbcc" -> abacbc
        # we want to track frquency and get the most freq occuring to use
        # we need key value store 

        count = {}
        maxHeap = []
        for char in s:
            if char in count:
                count[char] +=1
            else:
                count[char] = 1
        print (count)
        ## NOw that we have the hashMap, we can use MaxHeap for gettingthe most frequent
        ## lets append these values to heap
        for item in count:
            maxHeap.append([-count[item], item])
        

        heapq.heapify(maxHeap)

        ## now we have our maxHEap

        visited = None
        result = ""
        while maxHeap or visited:
            if visited and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt+=1

            if visited:
                heapq.heappush(maxHeap, visited)
                visited = None

            if cnt != 0:               ## if cnt == 0 then we dont stoer in prev, we used the char
                visited = [cnt,char]
        return result
