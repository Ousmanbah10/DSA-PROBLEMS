# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        parent_map = defaultdict(int)

        if not root.left and not root.right:
            return 0

        def parent_child(node):
            if not node:
                return
            if node.left:
                parent_map[node.left] = node
                parent_child(node.left)
            if node.right:
                parent_map[node.right] = node
                parent_child(node.right)    
        parent_child(root)

        def find_target(node, target):
            if not node:
                return None
            if node.data == target:  
                return node
            left_result = find_target(node.left, target)
            if left_result: 
                return left_result
            return find_target(node.right, target)
         
        target_node = find_target(root, start)
    
        visited = set()
        queue = deque([target_node])
        visited.add(target_node)
        count = 0

        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                
                if node in parent_map and parent_map[node] not in visited:
                    queue.append(parent_map[node])
                    visited.add(parent_map[node])

            if queue:  # fire spreads further → increment time
                count += 1

        return count