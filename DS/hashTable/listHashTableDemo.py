from hashTable.listHashTable import *

def main():
    print("List Hash Table Demo!")
    h = ListHashTable(11)
    h.insert(10)
    h.insert(21)
    #h.delete(20)   # 아무 영향 없어야 함
    h.insert(20)
    h.insert(5)
    h.insert(80)
    h.insert(32)
    h.printAll()

    h.delete(20)
    h.delete(80)

    # Just for checking purpose
    item = 21
    (i, j) = h.search(item)
    if i == None:
        print("Search Failed!")
    else:
        print("Search:", item, "List:", i, ", item index", j)

if __name__ == "__main__":
    main()