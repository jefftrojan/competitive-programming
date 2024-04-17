class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a = []

        for i in trips:
           
            a.append((i[2], 0, i[0])) 
            a.append((i[1], 1, i[0]))
        
        a.sort()
        cur = 0

        for i in a:
            if (i[1]):
                cur += i[2]
                if (cur > capacity):
                    return False
            else: 
                cur -= i[2]

        return True