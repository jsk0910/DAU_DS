import setuptools

setuptools.setup(
    include_package_data = True,
    name = "dsdau",
    version = "0.0.1.3",
    description = "DAU Data Structure Modules",
    author = "SangKyunJeon",
    author_email = "sangkyun.jeon@gmail.com",
    url = "https://github.com/jsk0910/DAU_DS",
    download_url = "https://github.com/jsk0910/DAU_DS/archive/refs/tags/v0.0.1.3.zip",
    install_requires = ['pytest'],
    py_modules = ['DS.list_.bidirectNode', 
                'DS.list_.circularDoublyLinkedList', 
                'DS.list_.circularDoublyLinkedListDemo', 
                'DS.list_.circularLinkedList',
                'DS.list_.circularLinkedListDemo',
                'DS.list_.linkedListBasic',
                'DS.list_.linkedListBasicDemo',
                'DS.list_.listNode',
                'DS.stack_.linkedStack',
                'DS.stack_.linkedStackDemo',
                'DS.stack_.listStack',
                'DS.stack_.listStackDemo',
                'DS.stack_.postfix',
                'DS.stack_.reverseString',
                'DS.sort_.bubbleSort',
                'DS.sort_.bubbleSortDemo',
                'DS.sort_.bucketSort',
                'DS.sort_.bucketSortDemo',
                'DS.sort_.countingSort',
                'DS.sort_.countingSortDemo',
                'DS.sort_.heapSort',
                'DS.sort_.heapSortDemo',
                'DS.sort_.insertionSort',
                'DS.sort_.insertionSortDemo',
                'DS.sort_.mergeSort',
                'DS.sort_.mergeSortDemo',
                'DS.sort_.quickSort',
                'DS.sort_.quickSortDemo',
                'DS.sort_.radixSort',
                'DS.sort_.radixSortDemo',
                'DS.sort_.selectionSort',
                'DS.sort_.selectionSortDemo',
                'DS.sort_.shellSort',
                'DS.sort_.shellSortDemo',
                'DS.queue_.linkedQueue',
                'DS.queue_.linkedQueueDemo',
                'DS.queue_.listQueue',
                'DS.queue_.listQueueDemo',
                'DS.queue_.palindrome',
                'DS.heap_.heap',
                'DS.heap_.heapDemo',
                'DS.hashTable_.chainedHashTable',
                'DS.hashTable_.chainedHashTableDemo',
                'DS.hashTable_.hashOpenAddressed',
                'DS.hashTable_.hashOpenAddressedDemo',
                'DS.hashTable_.listHashTable',
                'DS.hashTable_.listHashTableDemo',
                'DS.BST.AVLTree',
                'DS.BST.AVLTreeDemo',
                'DS.BST.binarySearchTree',
                'DS.BST.binarySearchTreeDemo'
                ],
    #package_dir = {"": "DS"},
    #packages=setuptools.find_packages(where='DS'),
    long_description = "Dong-A Univ. Data Structure Lecture Modules",
    long_description_content_type = "text/markdown",
    classifiers= [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)