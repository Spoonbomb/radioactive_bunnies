#!/usr/bin/env python3


from control_class import Control
import time

__version__ = '0.1'




def main_loop():
	
	controller = Control()
	controller.create_obj(5)

	while True:
		
		check = controller.update()
		if check == False:
			break
		time.sleep(2)


main_loop()
print('***Bunny population ceased***')

