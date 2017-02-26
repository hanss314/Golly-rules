def main():
	birth_string = list(input("Enter Birth Rules"))
	survive_string = list(input("Enter Survival Rules"))
	birth_rules = []
	survive_rules = []
	
	for c in birth_string:
		c_int = ord(c)-48
		if c_int<9 and c_int>0 and (c_int not in birth_rules):
			birth_rules.append(c_int)
			
	for c in survive_string:
		c_int = ord(c)-48
		if c_int<9 and c_int>=0 and (c_int not in survive_rules):
			survive_rules.append(c_int)
			
	birth_rules.sort()
	survive_rules.sort()
	
	name = "GOLAD_B"
	for i in birth_rules:
		name += str(i)
	name+="S"
	for i in survive_rules:
		name += str(i)
	
	writer = open(name+".rule",'w')
	writer.write(
		"@RULE "+name+"\n"+
		"@TABLE\n"+
		"n_states:4\n"+
		"neighborhood:Moore\n"+
		"symmetries:permute\n"+
		"var livingMaj={1,2}\n"+
		"var livingC={1,2,3}\n"
	)
	try:
		for i in range(survive_rules[-1]):
			writer.write(
				"var living"+str(i)+"={1,2,3}\n"
			)
	except:
		pass
		
	for i in range(8):
		writer.write(
			"var all"+str(i)+"={0,1,2,3}\n"+
			"var living"+str(i)+"={1,2,3}\n"
		)
	
	for birth in birth_rules:
		for majNumber in range(1,int(birth/2)+2):#colored births
			writer.write("0,")
			
			for i in range(majNumber):
				writer.write("livingMaj,")
				
			others = majNumber-1
			if birth%2==0:
				others -=1
			if others<0:
				others = 0
				
			for i in range(others):
				writer.write("living"+str(i)+",")
				
			for i in range(birth-majNumber-others):
				writer.write("3,")
			
			for i in range(8-birth):
				writer.write("0,")
				
			writer.write("livingMaj\n")
			
		for coloredNum in range(int(birth/2)+1):#neutral births
			writer.write("0,")
			
			for i in range(coloredNum):
				writer.write("1,2,")
				
			for i in range(birth-2*coloredNum):
				writer.write("3,")
			
			for i in range(8-birth):
				writer.write("0,")
			
			writer.write("3\n")
			
	for survive in survive_rules:
		writer.write("livingC,")
		
		for i in range(survive):
			writer.write("living"+str(i)+",")
			
		for i in range(8-survive):
			writer.write("0,")
			
		writer.write("livingC\n")
		
	writer.write(
		"livingC,all0,all1,all2,all3,all4,all5,all6,all7,0\n"  
		"@COLORS\n"+
		"1 255 0 0\n"+
		"2 0 0 255\n"+
		"3 255 255 255"
	)
	
	
if __name__ == "__main__":
    main()