#!/usr/bin/env python3

import random

class Bunny:
	def __init__(self):
		self.sex = self.set_sex()
		self.color  = self.set_color()
		self.age = 0
		self.name = self.set_name()
		self.radioactive = self.is_radioactive()
		
	def set_sex(self):
		sex = ['Female','Male']
		return random.choice(sex)
	
	def set_color(self):
		color = ['Brown', 'Black', 'White', 'Gray', 'Spotted', 'Blue', 
			'Californian', 'Castor', 'Cinnamon']
		return random.choice(color)
		
	def set_name(self):
		try:
			filer = open('names.txt')
			lines = filer.readlines()
			filer.close()
			line = random.choice(lines).strip()
			return line;
		except UnicodeDecodeError:
			filer = open('names2.txt')
			lines = filer.readlines()
			filer.close()
			line = random.choice(lines).strip()
			return line;
		
	def is_radioactive(self):
		randnum = random.randint(0,100)
		if randnum <= 2: # 2% chance of radioactive bunny
			return True
		else:
			return False
			
	
if __name__ == '__main__':
	def create_new(num):
		bunnies = [Bunny() for b in range(num)]
		for j in range(num):
			print(bunnies[j].__dict__.values())
		

	create_new(5)
	print('sep')
	create_new(10)




