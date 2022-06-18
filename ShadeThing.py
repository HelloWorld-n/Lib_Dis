#!/bin/python3
import random

class ShadeThing:
	def __init__(self, value_limits, value_steps = {"min": 0, "max":1}):
		self.value = value_limits["min"]
		self.value_limits = value_limits
		self.value_steps = value_steps

		if self.value_limits["min"] < 0 or self.value_limits["max"] < 0:
			raise Exception(f"""{''
				}Argument `value_limits` shell be dict with keys {{\"min\", \"max\"}}{''
				}such that value of`max` > value of `min`。{''
			}""")
		if self.value_steps["min"] < 0 or self.value_steps["max"] < 0:
			raise Exception(f"""{''
				}Argument `value_steps` shell be dict with keys {{\"min\", \"max\"}}{''
				}such that value of`max` > value of `min`。{''
			}""")
					
	def iterate(self):
		if self.value <= self.value_limits["min"]:
			self.isIncrementing = True
		if self.value >= self.value_limits["max"]:
			self.isIncrementing = False

		self.value += (
			+1 if self.isIncrementing else -1
		) * (
			random.randint(self.value_steps["min"], self.value_steps["max"])
		)
		
		if self.value < self.value_limits["min"]:
			self.value = self.value_limits["min"]
		if self.value > self.value_limits["max"]:
			self.value = self.value_limits["max"]
		
		return self.value
