class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_reference(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_reference(self, reference):
        self.next = reference


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def display_list_items(self):
        current = self.head
        while current is not None:
            print("{}".format(current.get_data()), end=" ")
            current = current.get_reference()

    def insert_node_at_beginning(self, value):
        temp = Node(value)
        temp.set_reference(self.head)
        self.head = temp
        self.size += 1
        print('Node item {} has been successfully added in beginning of the list'.format(value))

    def insert_node_at_end(self, value):
        temp = Node(value)
        current = self.head
        while current.get_reference() is not None:
            current = current.get_reference()
        current.set_reference(temp)
        self.size += 1
        print('Node item {} has successfully added to end of Linked List'.format(value))

    def search_item_in_list(self, value):
        found = False
        current = self.head
        while found is False and current:
            if current.get_data() == value:
                found = True
                print('{} is in the list'.format(value))
            else:
                current = current.get_reference()
        return found

    def delete_list_from_item(self, value):
        current = self.head
        previous = None
        found = False

        if current is None:
            print("List is Empty")

        while not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_reference()

        if previous is None:
            current = current.get_reference()
        else:
            previous.set_reference(current.get_reference())

        self.size -= 1

def main():
    mylist = LinkedList()
    while True:
        print("")
        print("Select an action among the followings:")
        print("1. Create a Singly Linked List.")
        print("2. Display List Nodes.")
        print("3. Insert an item in beginning of the list.")
        print("4. Insert an item at end of the list.")
        print("5. Search an item in the list.")
        print("6. Delete an item from the list.")
        print("7. Quit.")
        print("")

        choice = int(input("Enter your choice: "))
        print("")

        if choice == 7:
            print("Thanks!\n")
            break

        elif choice == 1:
            items = int(input("Enter the size of the list:"))
            for item in range(items):
                data = int(input("Enter the element:"))
                mylist.insert_node_at_beginning(value=data)
            mylist.display_list_items()

        elif choice == 2:
            mylist.display_list_items()

        elif choice == 3:
            item = int(input("Enter an item:"))
            print(mylist.insert_node_at_beginning(value=item))

        elif choice == 4:
            item = int(input("Enter an item:"))
            print(mylist.insert_node_at_end(value=item))

        elif choice == 5:
            item = int(input("Enter an item:"))
            mylist.search_item_in_list(value=item)

        elif choice == 6:
            item = int(input("Enter an item to delete from the list:"))
            mylist.delete_list_from_item(value=item)

        else:
            print("Invalid Reference! Please select the correct values")


if __name__ == '__main__':
    main()
