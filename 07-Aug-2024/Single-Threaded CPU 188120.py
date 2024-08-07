# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i , t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])

        res, minHeap = [], []
        i, current_time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and current_time >= tasks[i][0]: 
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i += 1

            if not minHeap:
                current_time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(minHeap)
                current_time += process_time
                res.append(index)

        return res