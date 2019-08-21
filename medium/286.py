
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #way1 slow
        # if not rooms:
        #     return 
        # m, n = len(rooms), len(rooms[0])
        # def update(i, j, dist, rooms):
        #     if 0 <= i < m and 0 <= j < n and rooms[i][j] >= dist:
        #         rooms[i][j] = dist
        #         update(i+1, j, dist+1, rooms)
        #         update(i-1, j, dist+1, rooms)
        #         update(i, j+1, dist+1, rooms)
        #         update(i, j-1, dist+1, rooms)
        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == 0:
        #             update(i, j, 0, rooms)
        #way2 slow
#         if not rooms:
#             return 
#         m, n = len(rooms), len(rooms[0])
        
#         def update(i, j, dist, rooms):
#             if rooms[i][j] >= dist:
#                 rooms[i][j] = dist
#                 for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
#                     if 0 <= r < m and 0 <= c < n:
#                         update(r, c, dist+1, rooms)
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     update(i, j, 0, rooms)
        #way3 
        if not rooms:
            return 
        m, n = len(rooms), len(rooms[0])
        q = [(i,j) for i in range(m) for j in range(n) if rooms[i][j] == 0]     
        for i,j in q:       #begin from 0, make it a 四叉树，change any neighbourhoods which is INF to [i][j]+!
            for r,c in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=r<m and 0<=c<n and rooms[r][c] >= 214748364:
                    rooms[r][c] = rooms[i][j] + 1
                    q.append((r,c))
        