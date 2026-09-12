class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base Case 1: Empty input returns None
        if not node:
            return None
        
        cloned = {}

        def dfs(curr: 'Node') -> 'Node':
            # If already cloned, return the cloned instance to preserve connections/cycles
            if curr in cloned:
                return cloned[curr]
            
            # Create clone and store in hash map BEFORE recursive calls
            copy = Node(curr.val)
            cloned[curr] = copy
            
            # Recursively copy all neighbors (handles empty neighbors list automatically)
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        return dfs(node)