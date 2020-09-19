import sys
import math

inp_file = sys.argv[1]

with open(inp_file) as f:
    lines = f.read().splitlines()
f.close()


tc = int(lines[0])
for x in range(1,tc+1):
	time = lines[x].split()
	h = int(time[0])
	m = int(time[1])
	s = int(time[2])
	a = int(time[3])
	b = int(time[4])
	c = int(time[5])

	theta = math.fabs((360 * (a * m * s - (h - 1) * (b * s + c))) / (h * m * s))
	angle = round(theta, 2)
	if angle <= 180:
		print(angle)
	else:
		print(360 - angle)
	


		
