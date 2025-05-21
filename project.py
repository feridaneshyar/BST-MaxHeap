class bstnode:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None
        self.parent = None 
class BST:
    def __init__(self):
     self.root = None
     
    def isEmptyBST(self):
        return self.root is None
 
    def insertrequest (self, id, name):
        node = bstnode(id,name)
        if not self.root :
            self.root = node
            return
        prev = None
        curr = self.root
        while curr:
            if curr.id < id:
                prev = curr
                curr = curr.right
            else :
                prev = curr
                curr = curr.left
        node.parent = prev
        if prev.id < id :
            prev.right = node
        else :
            prev.left = node

    def searchrequest(self, id):
        curr = self.root
        while curr:
            if  curr.id == id:
                return curr
            elif curr.id < id:
                curr = curr.right
            else :
                curr = curr.left
        return None
    
    def printBST(self):
     self.preorder(self.root)

    def preorder(self, node):
        if node:
            print(f"ID: {node.id}, Name: {node.name}")
            self.preorder(node.left)
            self.preorder(node.right)
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent
            
    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def deleteRequest(self, id):
        node = self.searchrequest(id)
        if node is None:
            return
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
        return node


        

            
 
class HeapNode:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority         
class MaxHeap:
    def __init__(self):
         self.heap = []
    def sizemaxheap(self):
        return len(self.heap)
    def isempty(self):
        if self.sizemaxheap():
            return False
        else:
            return True
    def insertHeap(self, id, priority):
        node = HeapNode(id,priority)
        self.heap.append(node)
        index = self.sizemaxheap() - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    def maxHeapify(self, index):
        n = self.sizemaxheap()
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left].priority > self.heap[index].priority:
            largest = left
        else:
            largest = index


        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.maxHeapify(largest)

   
            
    def deleteMaxHeap(self):
      
        if self.isempty():
            return None

        max_item = self.heap[0]
        last = self.heap.pop()

        if not self.isempty():
            self.heap[0] = last
            self.maxHeapify(0)
        return max_item
    
    def deleteRequest(self, id):
        index = self.sizemaxheap() - 1

        while index >= 0:
            if self.heap[index].id == id:
                break
            index -= 1

        if index == -1:
            print(f"Request with ID {id} not found in Heap.")
            return

        if index == self.sizemaxheap() - 1 :
            self.heap.pop()
            return

        self.heap[index] = self.heap.pop()

        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            while index > 0:
                parent = (index - 1) // 2
                if self.heap[index].priority > self.heap[parent].priority:
                    self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                    index = parent
                else:
                    break
        else:
            self.maxHeapify(index)
    

    
    def printMaxHeap(self):
            for node in self.heap:
                print(f"ID: {node.id}, Priority: {node.priority}")
                
  
    def increasePriority(self, id, newPriority):
    
        i = self.sizemaxheap() - 1 
        
        while i >= 0:
            if self.heap[i].id == id:
                
                
                
                break
            i -= 1 
        
        if i == -1: #not found
            return

    
        if newPriority <= self.heap[i].priority:  #old piority > new priority
            return

    
        self.heap[i].priority = newPriority
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i].priority > self.heap[parent].priority:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break
            
    def processHighestPriorityRequest(self, bst):
        request = self.deleteMaxHeap()
        if request:
            bst.deleteRequest(request.id)
         

# bst = BST()
# heap = MaxHeap()

# while True:
    
#     menu = '''\n<< menu >>
#     1. Insert Request
#     2. Search Request
#     3. Delete Request
#     4. Process Highest Priority Request
#     5. Increase Priority of Request
#     6. Print BST(Pre-order)
#     7. Print MaxHeap(Level-order)
#     8. Exit'''
#     print(menu)

#     choice = input("Enter your choice (1-8): ").strip()

#     if choice == '1':
#         try:
#             id = int(input("Enter Request ID: "))
#             name = input("Enter Request Name: ").strip()
#             priority = int(input("Enter Priority (integer): "))
#             bst.insertrequest(id, name)
#             heap.insertHeap(id, priority)
#             print("Request inserted successfully.")
#         except:
#             print("Invalid input, please try again.")

#     elif choice == '2':
#         try:
#             id = int(input("Enter Request ID to search: "))
#             node = bst.searchrequest(id)
#             if node:
#                 print(f"Request found. id = {id}, name = {node.name}.")
#             else:
#                 print(f"Request ID {id} not found in BST.")
#         except:
#             print("Invalid input, please try again.")
            
#     elif choice == '3':
#         try:
#             id = int(input("Enter Request ID to delete: "))
#             node = bst.deleteRequest(id)
#             if node:
#                 print(f"Request with ID {id} deleted from BST.")
#                 heap.deleteRequest(id)

#             else:
#                 print(f"Request ID {id} not found in BST.")
#         except:
#             print("Invalid input, please try again.")

#     elif choice == '4':
#         if heap.sizemaxheap == 0:
#             print("No requests to process.")
#         else:
#             heap.processHighestPriorityRequest(bst)
#             print("done.")

#     elif choice == '5':
#         try:
#             id = int(input("Enter Request ID to increase priority: "))
#             new_priority = int(input("Enter new Priority: "))
#             heap.increasePriority(id, new_priority)
#         except:
#             print("Invalid input, please try again.")

#     elif choice == '6':
#         print("\nBST contents (Pre-order traversal):")
#         bst.printBST()

#     elif choice == '7':
#         print("\nMaxHeap contents:")
#         heap.printMaxHeap()

#     elif choice == '8':
#         print("Exiting the program. Goodbye!")
#         break

#     else:
#         print("Invalid choice, please select a number between 1 and 8.")



