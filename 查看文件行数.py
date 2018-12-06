import os
line_count,blank_count=0,0
with open("a.txt") as fp:
	while True:
		line=fp.readline()
		if not line:
			break
		line_count+=1
		if  len(line.strip())==0:
			blank_count+=1
print(line_count,"Lines(",blank_count,"blanks)")#a文本中的行数
