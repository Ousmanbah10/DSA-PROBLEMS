from collections import defaultdict
class Solution:
    def isCycle(self, V, adj):
        
            
        parent = {}
        visited = set()

        def dfs(root,child):
            
            visited.add(root)
            parent[root] = child

            for element in adj[root]:

                if element not in visited:
                    

                    if dfs(element,root):
                        return True
                elif element in visited and parent[root] != element:
                    return True 

            return False

        for node in range(V):
            if node not in visited:  
                if dfs(node, None):  
                    return True
               
        return False    
            