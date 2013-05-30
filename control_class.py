#!/usr/bin/env python3
from bunny_class import Bunny
import time
import random

class Control():
	def __init__(self):
		self.bunny_obj_list = [] #list of bunny objects
		self.bunny_count = 0 #bunny object count
		self.loop_count = 2012 # year
		self.age_to_die = 9 # +1
		self.RA_number = 0 #number of bunnies with radiation
		self.total_old_death_count = 0
		self.total_RA_death_count = 0
		self.total_birth_count = 0
		self.female_count = 0
		self.starvation = 0
		
		
	def create_obj(self, num):
		for obj in range(num):
			bunny_obj = Bunny() #create obj
			self.bunny_obj_list.append(bunny_obj) #append obj to list of objects
			self.total_birth_count += 1
			self.bunny_count += 1
			if bunny_obj.radioactive:
					self.RA_number += 1
			self.output(bunny_obj, 'born')
			
	###update methods
	def count_update(self):
		pass
		#self.bunny_count = len(self.bunny_obj_list)
	
	def add_age_update(self):
		for obj in self.bunny_obj_list:
			obj.age += 1
	
	def kill_old_update(self):
		for obj in self.bunny_obj_list:
			if obj.age > self.age_to_die:
				index = self.bunny_obj_list.index(obj)
				dead_obj = self.bunny_obj_list.pop(index)
				if dead_obj.radioactive:
					self.RA_number -= 1
				self.total_old_death_count += 1
				self.bunny_count -= 1
				self.output(dead_obj, 'old')
				
	def RA_kills(self):
		#RA_num = 0
		#for obj in self.bunny_obj_list:
			#if obj.radioactive == True:
				#self.RA_number += 1
		#self.RA_number = RA_num
		if self.RA_number > 0: #if radiated bunnies, kill bunnies every loop
			for bun in range(self.RA_number):
				try:
					obj = random.choice(self.bunny_obj_list)
				except IndexError: #not sure why though
					return
				index = self.bunny_obj_list.index(obj)
				dead_obj = self.bunny_obj_list.pop(index)
				if dead_obj.radioactive:
					self.RA_number -= 1
				self.total_RA_death_count += 1
				self.bunny_count -= 1
				self.output(dead_obj, 'RA')
				
	def female_prego(self):
		#TODO need to create obj with properties of mother
		for obj in self.bunny_obj_list:
			if obj.sex == 'Female':
				self.female_count += 1
		if self.female_count > 0: #if prego bunnies, add bunnies for every loop
			self.create_obj(int(self.female_count / 4)) ###TOO MANY BUNNIES
			#self.create_obj(2)
			
		
				
					
	def output(self, obj, reason):

		if reason == 'born':
			reason_ = 'was born'
		elif reason == 'old':
			reason_ = 'has died of old age'
		elif reason == 'RA':
			reason_ = 'was killed by radiation'
			
			
		if obj.radioactive == True:
			RA = 'radioactive '
		else:
			RA = ''
		stringer = '{RA}Bunny {name} {reason} \n{sex} {color} \n'.format(
				reason=reason_,
				name=obj.name,
				sex=obj.sex,
				color=obj.color,
				RA=RA)
			
		print(self.header() + stringer)
		
		time.sleep(1)
		
	def header(self):
		header_ = ('-' * 25) + ' Year {}, Population {}, Radioactive {} \nTotal: Births {}, Elderly Deaths {}, Radioactive deaths {}, Mass Starvations {}\n'.format(
			self.loop_count, self.bunny_count, self.RA_number, self.total_birth_count, self.total_old_death_count, self.total_RA_death_count, self.starvation) +'\n' 
		return header_
		
	def check_population(self):
		if self.bunny_count > 1000:
			hunger = int(len(self.bunny_obj_list) / 2)
			for bun in range(hunger):
				obj = random.choice(self.bunny_obj_list)
				index = self.bunny_obj_list.index(obj)
				dead_obj = self.bunny_obj_list.pop(index)
				if dead_obj.radioactive:
					self.RA_number -= 1
					
				self.starvation += 1
				self.bunny_count -= 1
				#self.output(dead_obj, 'starve')
			print('***{} bunnies died from starvation'.format(hunger))
			
		elif self.bunny_count <= 1:
			return False
		
		
	def update(self):
		
		self.RA_kills()
		self.add_age_update()
		self.kill_old_update()
		self.female_prego()

		check = self.check_population()
		if check == False:
			return False
		
		
		self.count_update()
		self.loop_count += 1
		
