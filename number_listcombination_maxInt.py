'''
This problem was asked by Twitter.

Given a list of numbers, create an program that arranges
them in order to form the largest possible integer.
For example,
given [10, 7, 76, 415], you should print 77641510

sample input
[10, 7, 76, 415]
sample output
77641510
'''

lst = eval(input())
# string list
lst_new = list(map(str, lst))


from itertools import permutations
p=list(permutations(lst_new))
max=0
for i in p:
	s=""
	for j in i:
		s=s+j
	if int(s)>max:
		max=int(s)
print(max)


