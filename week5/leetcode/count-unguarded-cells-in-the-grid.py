class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        count = set()
        wall = {(i, j) for i, j in walls}
        guard = {(i, j) for i, j in guards}

        for g in guards:
            r, c = g
            for cc in range(c + 1, n):
                if (r, cc) not in guard and (r, cc) not in wall:
                    count.add((r, cc))
                else:
                    break

            for cc in range(c - 1, -1, -1):
                if (r, cc) not in guard and (r, cc) not in wall:
                    count.add((r, cc))
                else:
                    break

            for rr in range(r + 1, m):
                if (rr, c) not in guard and (rr, c) not in wall:
                    count.add((rr, c))
                else:
                    break

            for rr in range(r - 1, -1, -1):
                if (rr, c) not in guard and (rr, c) not in wall:
                    count.add((rr, c))
                else:
                    break

        print(count)
        return m * n - len(guards) - len(walls) - len(count)

