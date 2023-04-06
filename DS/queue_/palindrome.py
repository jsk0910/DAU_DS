from stack.listStack import *
from queue_.listQueue import *

def isPalindrome(A) -> bool:
	s = ListStack(); q = ListQueue()
	for i in range(len(A)):
		s.push(A[i]); q.enqueue(A[i])
	while (not q.isEmpty()) and s.pop() == q.dequeue():
		{}
	if q.isEmpty():
		return True
	else:
		return False

def main():
	print("Palindrome Check!")
	str = 'lioninoil' # 테스트 문자열
	t = isPalindrome(str)
	print(str, " is Palindrome?: ", t)

if __name__ == "__main__":
	main()

# 코드 7-15