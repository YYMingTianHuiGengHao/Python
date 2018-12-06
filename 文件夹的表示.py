
#输出当前目录下的文件和文件夹

import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))
for root,dirs,files in os.walk(root_path):
	current_path = root.split("\\")
	level = len(current_path) - offset
	print("\t"*level,current_path[-1])
	for f in files:
		print("\t"*(level+1),f)