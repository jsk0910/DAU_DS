from stack.listStack import *

st1 = ListStack()
print(st1.top())	# No effect
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty?', st1.isEmpty())

# 코드 6-7