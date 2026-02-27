mahasiswa = [
    {
        "NIM": "25032014003",
        "Nilai": 90
    },
    {
        "NIM": "25032014006",
        "Nilai": 88
    },
    {
        "NIM": "25032014007",
        "Nilai": 92
    },
    {
        "NIM": "25032014008",
        "Nilai": 85
    },
    {
        "NIM": "25032014009",
        "Nilai": 91
    },
    {
        "NIM": "25032014010",
        "Nilai": 87
    },
    {
        "NIM": "25032014011",
        "Nilai": 89
    },
    {
        "NIM": "25032014012",
        "Nilai": 93
    },
    {
        "NIM": "25032014013",
        "Nilai": 86
    },
    {
        "NIM": "25032014014",
        "Nilai": 94
    }
]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printNode(self):
        node = self.head
        id = 1

        while node:
            data = node.data

            print(f"\nMahasiswa {id}")
            print(f"NIM   : {data['NIM']}")
            print(f"Nilai : {data['Nilai']}")
            print("-" * 10)

            node = node.next
            id += 1

    def addMHS(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def sortingNilai(self):
        current = self.head

        while current:
            max_node = current
            next_node = current.next

            while next_node:
                if next_node.data["Nilai"] > max_node.data["Nilai"]:
                    max_node = next_node
                next_node = next_node.next

            # tukar data
            current.data, max_node.data = max_node.data, current.data
            current = current.next

    def averageNilai(self):
        total = 0
        count = 0

        node = self.head
        while node:
            total += node.data["Nilai"]
            count += 1
            node = node.next

        return total / count if count > 0 else 0
    
    def highestNilai(self):
        if not self.head:
            return

        max_node = self.head
        node = self.head.next

        while node:
            if node.data["Nilai"] > max_node.data["Nilai"]:
                max_node = node
            node = node.next

        return max_node.data

linklist = LinkedList()

for mhs in mahasiswa:
    linklist.addMHS(mhs)

print("___ DATA AWAL ___")
linklist.printNode()

print("\n___ Urutan Nilai Tertinggi ke Terendah ___")
linklist.sortingNilai()
linklist.printNode()

print("\n___ RATA-RATA ___")
print(linklist.averageNilai())

print("\n___ NILAI TERTINGGI ___")
print(linklist.highestNilai())

## kompleksitas waktu
## function addMHS = O(1)
## function sortingNilai = O(n^2)
## function highestNilai = O(n)