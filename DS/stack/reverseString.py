from stack.listStack import *

def reverse(str):
	st = ListStack()
	for i in range(len(str)):
		st.push(str[i])
	out = ""
	while not st.isEmpty():
		out += st.pop()
	return out

def main():
	input = "Test Seq 12345"  # 테스트 입력 문자열 String
	answer = reverse(input)
	print("Input string: ", input)
	print("Reversed string: ", answer)

if __name__ == "__main__":
	main()

# 코드 6-15