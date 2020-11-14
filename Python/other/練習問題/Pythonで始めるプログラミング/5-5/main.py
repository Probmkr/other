print('\n(1)')

nums = [10,20,30,40,50]
print(nums,end = '->')
for i in range(len(nums)):
	nums[i] -= 30

print(nums,end = '\n\n(2)\n')

words = ['love','like','hate']
print(words,end = '->')
for i in range(len(words)):
	words[i] = 'I ' + words[i] + ' you.'

print(words)