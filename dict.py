dictionary = {'hello':3,'world':8}
word = 'divi'
count = 3
dictionary.update({word:count})
values_2 = sorted(dictionary, key=dictionary.__getitem__, reverse=True)

for key in values_2:
	print key
#for key, value in dictionary.items():
#	print key, value

