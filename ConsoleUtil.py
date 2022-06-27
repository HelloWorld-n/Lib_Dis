#!/bin/python3


esc = "\u001B"

def applyBackgroundColor(red, green, blue):
	print(end = f"{esc}[48;2;{red};{green};{blue}m")

def applyForegroundColor(red, green, blue):
	print(end = f"{esc}[38;2;{red};{green};{blue}m")

def applyDefaultColors():
	print(end = f"{esc}[00m")

