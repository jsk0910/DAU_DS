import setuptools

setuptools.setup(
    include_package_data = True,
    name = "dsdau",
    version = "0.0.1.2",
    description = "DAU Data Structure Modules",
    author = "SangKyunJeon",
    author_email = "sangkyun.jeon@gmail.com",
    url = "https://github.com/jsk0910/DAU_DS",
    download_url = "https://github.com/jsk0910/DAU_DS/archive/refs/tags/v0.0.1.2.zip",
    install_requires = ['pytest'],
    py_modules = ['list.bidirectNode', 
                'list.circularDoublyLinkedList', 
                'list.circularDoublyLinkedListDemo', 
                'list.circularLinkedList',
                'list.circularLinkedListDemo',
                'list.linkedListBasic',
                'list.linkedListBasicDemo',
                'list.listNode',
                'stack.linkedStack',
                'stack.linkedStackDemo',
                'stack.listStack',
                'stack.listStackDemo',
                'stack.postfix',
                'stack.reverseString',
                'sort.bubbleSort',
                'sort.bubbleSortDemo',
                'sort.bucketSort',
                'sort.bucketSortDemo',
                'sort.countingSort',
                'sort.countingSortDemo',
                'sort.heapSort',
                'sort.heapSortDemo',
                'sort.insertionSort',
                'sort.insertionSortDemo',
                'sort.mergeSort',
                'sort.mergeSortDemo',
                'sort.quickSort',
                'sort.quickSortDemo',
                'sort.radixSort',
                'sort.radixSortDemo',
                'sort.selectionSort',
                'sort.selectionSortDemo',
                'sort.shellSort',
                'sort.shellSortDemo',
                'queue_.linkedQueue',
                'queue_.linkedQueueDemo',
                'queue_.listQueue',
                'queue_.listQueueDemo',
                'queue_.palindrome',
                'heap_.heap',
                'heap_.heapDemo',
                'hashTable.chainedHashTable',
                'hashTable.chainedHashTableDemo',
                'hashTable.hashOpenAddressed',
                'hashTable.hashOpenAddressedDemo',
                'hashTable.listHashTable',
                'hashTable.listHashTableDemo',
                'BST.AVLTree',
                'BST.AVLTreeDemo',
                'BST.binarySearchTree',
                'BST.binarySearchTreeDemo'
                ],
    package_dir = {"": "DS"},
    packages=setuptools.find_packages(where='DS'),
    long_description = "Dong-A Univ. Data Structure Lecture Modules",
    long_description_content_type = "text/markdown",
    classifiers= [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)