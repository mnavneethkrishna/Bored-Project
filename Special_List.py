#Just for fun!
"""This is a sequence of numbers in a list which are generated
in a special manner. The consecutive numbers follow an 
oscillating pattern such that the recently entered number 
occupies the left most position and the number previously 
entered will occupy the right most position.

Created by Navneeth Krishna (mnkb20@gmail.com)

"""

print(__doc__)
print("\n")
a = []
i = 1
while i <= 10 :
	a.reverse()
	print(a)
	a.append(i)
	i += 1
