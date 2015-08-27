import copy
src = raw_input("")
dst = raw_input("")
s = open(src , "r")
dt = open(dst , "w")
for l in s:
	newList=[]
	oldList= l.split()
	for found in oldList:
		if found != "eax" and found != "ebx" and found!="ecx" and found!="edx" and found!=",eax" and found!=",ebx" and found!=",ecx" and found!=",edx":
			newList.append(found)	
		if found == "eax":			
			newList.append("rax")
		elif found == "ebx":
			newList.append("rbx")
		elif found == "ecx":
			newList.append("rcx")
		elif found == "edx":
			newList.append("rdx")	
		elif found == "eax,":
			newList.append("rax,")
		elif found == "ebx,":
			newList.append("rbx,")
		elif found == "ecx,":
			newList.append("rcx,")
		elif found == "edx,":
			newList.append("rdx,")
	toBe = ' '.join(str(e) for e in newList)
	dt.write(toBe+"\n")
