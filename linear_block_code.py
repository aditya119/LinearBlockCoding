def check_wrong_dataword(dataword):
	if len(dataword) != 4:
		return 1
	for char in dataword:
		if char != '0' and char != '1':
			return 2
	return 0

def input_datawords(number_of_words):
	datawords = []
	for i in range(number_of_words):
		result = 3
		while result != 0:
			dataword = input('enter the dataword: ')
			result = check_wrong_dataword(dataword)
			if result == 1:
				print('all datawords should be of length 4')
			elif result == 2:
				print('a dataword should be made up of only 0s and 1s')
		datawords.append(dataword)
		print()
	return datawords

def generate_codewords(datawords):
	codewords = []
	for dataword in datawords:
		count1 = dataword.count('1')
		if count1 % 2 == 0:
			dataword += '0'
		else:
			dataword += '1'
		codewords.append(dataword)
	return codewords

def get_valid_codewords_list():
	valid_codewords_list = []
	with open('list.txt') as file:
		for i in range(16):
			string = file.readline()
			valid_codewords_list.append(string[:-1])
	file.close()
	return valid_codewords_list

def xor(bit1, bit2):
	if bit1 == '0' and bit2 == '0':
		return str(0)
	elif bit1 == '1' and bit2 == '1':
		return str(0)
	else:
		return str(1)

def xor_of_codewords(code1, code2):
	xor_result = ''
	for i in range(len(code1)):
		xor_result += xor(code1[i], code2[i])
	return xor_result

def main():
	print('4B/5B Linear Block Coding\n\n')
	
	datawords = input_datawords(int(input('enter number of words: ')))
	codewords = generate_codewords(datawords)
	
	valid_codewords_list = get_valid_codewords_list()
	for code in codewords:
		print(str(code), end=' ')
		if code in valid_codewords_list:
			print('valid')
		else:
			print('invalid')
	
	print('\nenter indices of the two words to find xor (index from 1 to '+str(len(codewords))+'):')
	i = 100
	j = 100
	while i not in range(1, len(codewords)+1):
		i = int(input('first word: '))
	print()
	while j not in range(1, len(codewords)+1) or j == i:
		j = int(input('second word: '))
	print()
	xor_result = xor_of_codewords(codewords[i-1], codewords[j-1])
	print(codewords[i-1]+' xor '+codewords[j-1]+' = '+xor_result)
	if xor_result in valid_codewords_list:
		print('it is also a valid codeword')
	else:
		print('xor has generated an invalid codeword')

if __name__ == '__main__':
	main()