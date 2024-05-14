class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        array = [i for i in range(n)]
        
        for i in range(len(edges)):
            if array[edges[i][1]] != array[edges[i][0]]:
                temp = array[edges[i][1]]
                for j in range(len(array)):
                    if array[j] == temp:
                        array[j] = array[edges[i][0]]
        
        return len(list(set(array)))