# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        
        nodes, answer = deque(), []
        nodes.append(root)
        
        while nodes:
            node = nodes.popleft()
            
            if node:
                answer.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                answer.append(None)
        
        # remove trailing nulls
        i = len(answer) - 1
        while answer[i] == None:
            i -= 1
        return answer[:i+1]
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) is 0:
            return None
        
        # add None leaves to the actual leaves
        i = len(data) - 1
        while i >= 0 and data[i] != None:
            i -= 1
        data = data + [None] * (len(data) - i - 1) * 2
        
        
        values = deque(data)
        head, fathers = TreeNode(values.popleft()), deque()
        fathers.append(head)
        while values:
            # make sure that we don't pop from empty lists
            if values:
                value1 = values.popleft()
                node1 = TreeNode(value1) if value1 != None else None
            if values:
                value2 = values.popleft()
                node2 = TreeNode(value2) if value2 != None else None
            # if there is a father, there must be 2 children
            if fathers:
                father = fathers.popleft()
                father.left, father.right = node1, node2
            
                if node1 != None:
                    fathers.append(node1)
                if node2 != None:
                    fathers.append(node2)
                    
        return head
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
