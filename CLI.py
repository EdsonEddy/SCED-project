from sced import SCED
from utils import *
from IPython import display

header = """
Welcome to SCED program CLI

░██████╗░█████╗░███████╗██████╗░
██╔════╝██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝█████╗░░██║░░██║
░╚═══██╗██║░░██╗██╔══╝░░██║░░██║
██████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░░╚════╝░╚══════╝╚═════╝░

"""
menu = """
Enter an option:
1. Group mode: Using Union Find Disjoint Sets
2. Group mode: All Pairs
3. Pair mode
4. Exit
"""

sub_menu = """
Enter an option:
1. Create results directory with results (document html)
2. Done
"""

sw = True

print(header)
while sw:
	print(menu)
	option = int_convert(input("Enter an option: "))
	if option == 1 or option == 2:
		directory_path = input("Enter directory full path: ")
		percentage = int_convert(input("Enter a percentage: "))
		if valid_path(directory_path) and percentage:
			program = SCED(directory_path, percentage)
			if option == 1:
				results = program.group_mode()
			else:
				results = program.allpair_mode()
			show_all_results(results)
			sw_2 = True
			while sw_2:
				print(sub_menu)
				sub_option = int_convert(input("Enter an option: "))
				if sub_option == 1:
					create_all_results(directory_path, results)
					sw_2 = False
				elif sub_option == 2:
					sw_2 = False
				else:
					print("Invalid option")
		else:
			print("Invalid path or percentage")
	elif option == 3:
		file_path_a = input("Enter file path A: ")
		file_path_b = input("Enter file path B: ")
		if valid_file_path(file_path_a) and valid_file_path(file_path_a):
			program = SCED(file_path_a, file_path_b)
			results = program.pair_mode()
			show_result(results)
		else:
			print("Invalid file paths")
		
	elif option == 4:
		sw = False
		print("Goodbye!")
	else:
		print("Invalid input")