import sys
import math

inp_file = sys.argv[1]

boys = []

with open(inp_file, "r") as f:
    boys = f.read().split()

gift_count = {}
for boy in boys:
	if boy in gift_count:
		gift_count[boy] += 1
	else:
		gift_count[boy] = 1

max_gifts = max(gift_count.values())

for key, value in gift_count.items(): 
	if value == max_gifts:
		print(key)
		break