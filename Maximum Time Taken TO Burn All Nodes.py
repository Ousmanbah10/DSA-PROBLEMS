# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        from collections import defaultdict
        parent_map = defaultdict(int)

        if not root.left and not root.right:
            return 0

        def parent_child(node):

            if not node:
                return

            if node.left:
                parent_map[node.left] = node
                left = parent_child(node.left)

            if node.right:
                parent_map[node.right] = node
                right = parent_child(node.right)    
             
                    
        parent_child(root)

        def find_target(node, target):
            
            if not node:
                return None

            if node.data == target:  
                return node

            left_result = find_target(node.left, target)
            right_result = find_target(node.right, target)
            return left_result or right_result
         

        target_node = find_target(root,start) 
    
        visited = set()
        queue = deque()
        queue.append(target_node)
        count = 0

        while queue:

            qlen = len(queue)

            
            for i in range(len(queue)):
                
                node = queue.popleft()
                # Add left kid 
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                # Add right
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
                
            count += 1
        return count - 1
