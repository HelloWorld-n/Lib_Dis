#!/bin/python3
import dis
from ShadeThing import ShadeThing

esc = "\u001B"

def gradientalColorThing():
	global shadeThing
	try:
		shadeThing
	except NameError:
		shadeThing = {
			"red": ShadeThing({"min": 128, "max": 255}, value_steps = {"min": 0, "max": 10}),
			"green": ShadeThing({"min": 128, "max": 255}, value_steps = {"min": 0, "max": 10}),
			"blue": ShadeThing({"min": 128, "max": 255}, value_steps = {"min": 0, "max": 10}),
		}
	return {x: shadeThing[x].iterate() for x in shadeThing.keys()}



if __name__ == "__main__":
	print(f"{esc}[48;2;0;0;0m")
	print(f"{esc}[38;2;255;255;255m")
	dis_instructions = dis.get_instructions(dis.get_instructions)
	for dis_instruction in dis_instructions:	
		rgb = gradientalColorThing()	
		print(end = f"{esc}[38;2;{rgb['red']};{rgb['green']};{rgb['blue']}m")
		print(f"""{
			dis_instruction.opname
		} ({dis_instruction.opcode}{
			(
				', ' + str(dis_instruction.argval)
			if dis_instruction.argval != None else
				''
			)
		})""")
