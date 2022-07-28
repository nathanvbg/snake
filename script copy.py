import pygame
import sys
import random

def print_map(snake_map):
	for i in range (0, 8):
		print(*snake_map[i])

def init():
	snake_map = [['--------'], ['|      |'], ['|      |'], ['|      |'], ['|      |'],
				 ['|      |'], ['|      |'], ['--------']]
	return(snake_map)

def play():
	print('ceeeeee partiiii')
	snake_map = init()
	print_map(snake_map)

if __name__ == "__main__" :
	play()