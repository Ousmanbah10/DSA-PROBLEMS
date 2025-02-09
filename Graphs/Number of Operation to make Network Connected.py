from collections import defaultdict
def makeConnected( n, connections) -> int:

        graph = defaultdict(list)
        
        connected = 0
        lines = 0
        for element in connections:

            source, destination = element[0],element[1]
            graph[source].append(destination)
            graph[destination].append(source)
            lines += 1

        
        visited = set()
        
        output = []
        def dfs(node,i,val):
            
            val += 1
            
            if node in visited:
                
                return i, val

            visited.add(node)
            i += 1
            for edge in graph[node]:
                
                i, val = dfs(edge, i , val)
                

            return i,val   
        extra = 0
        for node in range(n):
            
            if node not in visited:
                nodes, value = dfs(node, 0, 0)
                
                edges = value // 2
                
                
                if edges > nodes - 1:  
                    extra += edges - (nodes - 1)    
                    
                connected += 1
        print(extra) 

        if extra >= (connected - 1):
            return connected - 1
        else:
            return -1  