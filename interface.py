from project import BST,MaxHeap
bst = BST()
heap = MaxHeap()


while True:
    
    menu = '''\n<< menu >>
    1. Insert Request
    2. Search Request
    3. Delete Request
    4. Process Highest Priority Request
    5. Increase Priority of Request
    6. Print BST(Pre-order)
    7. Print MaxHeap(Level-order)
    8. Exit'''
    print(menu)

    choice = input("Enter your choice (1-8): ").strip()

    if choice == '1':
        try:
            id = int(input("Enter Request ID: "))
            name = input("Enter Request Name: ").strip()
            priority = int(input("Enter Priority (integer): "))
            bst.insertrequest(id, name)
            heap.insertHeap(id, priority)
            print("Request inserted successfully.")
        except:
            print("Invalid input, please try again.")

    elif choice == '2':
        try:
            id = int(input("Enter Request ID to search: "))
            node = bst.searchrequest(id)
            if node:
                print(f"Request found. id = {id}, name = {node.name}.")
            else:
                print(f"Request ID {id} not found in BST.")
        except:
            print("Invalid input, please try again.")
            
    elif choice == '3':
        try:
            id = int(input("Enter Request ID to delete: "))
            node = bst.deleteRequest(id)
            if node:
                print(f"Request with ID {id} deleted from BST.")
                heap.deleteRequest(id)

            else:
                print(f"Request ID {id} not found in BST.")
        except:
            print("Invalid input, please try again.")

    elif choice == '4':
        if heap.sizemaxheap == 0:
            print("No requests to process.")
        else:
            heap.processHighestPriorityRequest(bst)
            print("done.")

    elif choice == '5':
        try:
            id = int(input("Enter Request ID to increase priority: "))
            new_priority = int(input("Enter new Priority: "))
            heap.increasePriority(id, new_priority)
        except:
            print("Invalid input, please try again.")

    elif choice == '6':
        print("\nBST contents (Pre-order traversal):")
        bst.printBST()

    elif choice == '7':
        print("\nMaxHeap contents:")
        heap.printMaxHeap()

    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice, please select a number between 1 and 8.")