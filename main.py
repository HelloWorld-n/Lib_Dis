#!/bin/python3
import dis
from ShadeThing import ShadeThing
import ConsoleUtil

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


def inspect(functions):
	ConsoleUtil.applyBackgroundColor(0, 0, 0)
	ConsoleUtil.applyForegroundColor(255, 255, 255)
	for item in functions:
		dis_instructions = dis.get_instructions(item)
		rgb = gradientalColorThing()
		ConsoleUtil.applyForegroundColor(rgb["red"], rgb["green"], rgb["blue"])
		print(f"{item}")
		for dis_instruction in dis_instructions:	
			rgb = gradientalColorThing()
			ConsoleUtil.applyForegroundColor(rgb["red"], rgb["green"], rgb["blue"])
			print(f"""\t{
				dis_instruction.opname
			} ({
				(
					str(dis_instruction.argval)
				if dis_instruction.argval != None else
					''
				)
			})""")
		print()
	ConsoleUtil.applyDefaultColors()

if __name__ == "__main__":
	inspect([
		dis.get_instructions, 
		gradientalColorThing,
	])
