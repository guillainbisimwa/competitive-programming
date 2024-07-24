class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
    
        point = 0
        lacal_gas = 0
        total_gas = 0
        total_cost = 0
        
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            lacal_gas += gas[i] - cost[i]
            
            if lacal_gas < 0:
                point = i + 1
                lacal_gas = 0
        
        if total_gas - total_cost < 0:
            return -1
        
        return point
        