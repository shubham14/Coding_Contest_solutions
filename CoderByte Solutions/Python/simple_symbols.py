letters = 'abcdefghijklmnopqrstuvwxyz'
def SimpleSymbols(str):
	for i, ele in enumerate(str):
		if i == 0 and ele in letters:
			return "false"
		elif ele in letters and str[i - 1] == '+' and str[i + 1] == '+':
			return "true"
	return "false"

print SimpleSymbols(raw_input())