class BlackMoneyHolder:
	## write your code here
    
	def __init__(self,name,account_info):
		if name == None:
			raise TypeError("Name can't be None")
		elif not type(name) is str:
			raise TypeError("Name is not string")
		elif not (name and name.strip()):
			raise TypeError("Name is empty")
		elif type(account_info) != dict:
			raise TypeError("account_info is not a dictinary")
		else:
			self.name = name;
			self.account_info = account_info
		
	def update_amount(self,account_name,amount):
		if account_name in self.account_info:
			self.account_info[account_name] = self.account_info[account_name] + amount
		else:
		 	self.account_info[account_name] = amount
	 	
	def total_black_money(self):
		sum = 0
		for v in self.account_info.values():
			sum = sum + v
		return sum

	def __str__(self):
		str1 = ""
		helperDict = dict(sorted(self.account_info.items()))
		for k,v in helperDict.items():
			str1 += k + ": " + str(v) + "\n"
		return str1 
		
	def __len__(self):
		return len(self.account_info)
		
	def __getitem__(self,index):
		helperDict = dict(sorted(self.account_info.items()))
		list1 = [(k,v) for k,v in helperDict.items()]
		return list1[index];
		
	def __eq__(self,other):
		return self.total_black_money() == other.total_black_money()
	
	def __lt__(self,other):
		return self.total_black_money() < other.total_black_money()
		
	def __gt__(self,other):
		return self.total_black_money() > other.total_black_money()
		

