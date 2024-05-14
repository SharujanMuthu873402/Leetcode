class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        array = [i for i in range(n)]
        
        for i in range(len(edges)):
            if array[edges[i][1]] != array[edges[i][0]]:
                temp = array[edges[i][1]]
                for j in range(len(array)):
                    if array[j] == temp:
                        array[j] = array[edges[i][0]]
        
        print(array)
        return len(list(set(array))) == 1