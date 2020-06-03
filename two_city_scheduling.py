class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lst = []
        n = len(costs)//2
        minCost = 0
        for A, B in costs:
            lst.append(B - A)
            minCost += A
        lst.sort()
        for i in range(n):
            minCost += lst[i]
        return minCost
