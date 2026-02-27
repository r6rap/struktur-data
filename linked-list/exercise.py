class Node:
    def __init__(self, data):
        self.data = data
        self.next = None ## data selanjutnya pasti none

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        current_node = self.head
        while(current_node):
            print("Data: ", current_node.data, "Next: ", current_node.next)
            current_node = current_node.next

    def insertBeginning(self, new_data):
        new_node = Node(new_data) ## inisialisasi node baru
        new_node.next = self.head ## node selanjutnya diisi head lama
        self.head = new_node ## head sekarang diisi node baru

    def insertLast(self, new_data):
        new_node = Node(new_data)
        if self.head is None: ## jika head kosong
            self.head = new_node ## isi head dengan node baru
            return
        last = self.head ## last diisi head
        while last.next: ## loop sampai berada di data next
            last = last.next ## ubah iinsialisasi last dengan data next (None)
        last.next = new_node ## data next diisi node baru

    def insertAfter(self, previous_node, new_data):
        if previous_node is None: ## node sebelumnya harus ada
            print("prev node harus ada di linklist")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next ## node next diisi dengan data node sebelumnya
        previous_node.next = new_node ## pointer node sebelumnya dipindah ke node baru

    def deleteFirstNode(self):
        if self.head is None:
            print("LinkedList empty")
            return
        removed_node = self.head ## inisialisasi head
        self.head = self.head.next ## ubah data head dengan data selanjutnya
        removed_node.next = None ## mengubah data setelah head menjadi none (isolated node)
        
    def deleteLastNode(self):
        if self.head.next is None: ## kondisi jika hanya ada satu node
            self.head = None
        prev_node = None
        last = self.head
        while last.next:
            prev_node = last
            last = last.next
        prev_node
        last.next = None

linklist = LinkedList()
linklist.head = Node(1)
second = Node(2)
third = Node(3)

linklist.head.next = second
second.next = third

linklist.insertBeginning(9)
linklist.insertLast(10)
linklist.insertAfter(second, 17)
linklist.deleteFirstNode()
linklist.deleteLastNode()

print(linklist.printList())
print("Head: ", linklist.head.data, "Head next: ", linklist.head.next)