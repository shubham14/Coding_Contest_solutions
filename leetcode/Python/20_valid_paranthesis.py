class Solution:
	def isValid(self, s):
		pair_dict = [('(', ')'), ('{', '}'), ('[', ']')]
		stack = []
		for char in s:
			try:
				top = stack[0]
				if top == '(' and char == ')':
					stack.insert(0, char)
					stack.pop()
					stack.pop()
					print(stack)
				elif top == '{' and char == '}':
					stack.insert(0, char)
					stack.pop()
					stack.pop()
					print(stack)
				elif top == '[' and char == ']':
					stack.insert(0, char)
					stack.pop()
					stack.pop()
					print(stack)
				else:
					stack.insert(0, char)
			except IndexError:
				stack.insert(0, char)
		if len(stack) == 0:
			return True
		return False

if __name__ == "__main__":
	str1 = '{[]}'
	print(str1)
	sol = Solution()
	print(sol.isValid(str1))