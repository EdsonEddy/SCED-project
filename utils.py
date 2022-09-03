import os
import argparse
import difflib
import sys

# valid single file path
def valid_file_path(path):
	try:
		result = os.path.isfile(path)
		return True
	except Exception as e:
		return False

# valid file path
def valid_path(path):
	try:
		result = os.listdir(path)
		return True
	except Exception as e:
		return False

# try convert integer
def int_convert(value):
	try:
		integer = int(value)
		return integer
	except Exception as e:
		return False

# show results
def show_all_results(results):
	print("showing results...")
	for row in results:
		for col in row:
			print(col, end=" ")
		print()

# create results dir
def clean_results_dir():
	current_path = os.path.abspath(os.getcwd())
	results_path = os.path.join(current_path, "results")
	try:
		os.mkdir(results_path)
	except Exception as e:
		pass
	current_path = os.path.abspath(os.getcwd())
	results_path = os.path.join(current_path, "results")
	for root, dirs, files in os.walk(results_path):
	    for f in files:
	        os.unlink(os.path.join(root, f))
	    for d in dirs:
	        shutil.rmtree(os.path.join(root, d))

def create_result(old_file, new_file, output_file):
	file_1 = open(old_file, "r").readlines()
	file_2 = open(new_file, "r").readlines()
	if output_file:
		delta = difflib.HtmlDiff(tabsize = 2)
		with open(output_file, "w") as f:
			html = delta.make_file(fromlines = file_1, tolines = file_2, fromdesc = old_file, todesc = new_file)
			f.write(html)

def create_all_results(directory_path, results):
	clean_results_dir()
	current_path = os.path.abspath(os.getcwd())
	results_path = os.path.join(current_path, "results")
	for result in results:
		if len(result) == 2:
			name_file = result[0] + " " + result[1] + ".html"
		else:
			name_file = result[0] + " " + result[1] + str(result[2]).replace(".", ",") + ".html"
		output_file = os.path.join(results_path, name_file)
		file_a = os.path.join(directory_path, result[0])
		file_b = os.path.join(directory_path, result[1])
		create_result(file_a, file_b, output_file)
	print("results created in ", results_path)


def show_result(results):
	clean_results_dir()
	print("showing result...")
	result_a = results[0].split(os.sep)[-1]
	result_b = results[1].split(os.sep)[-1]
	percentage = results[2]
	print(result_a, result_b, percentage)
	file_1 = open(results[0], "r").readlines()
	file_2 = open(results[1], "r").readlines()
	current_path = os.path.abspath(os.getcwd())
	results_path = os.path.join(current_path, "results")
	name_file = result_a + " " + result_b + ".html"
	output_file = os.path.join(results_path, name_file)
	if output_file:
		delta = difflib.HtmlDiff(tabsize = 2)
		with open(output_file, "w") as f:
			html = delta.make_file(fromlines = file_1, tolines = file_2, fromdesc = results[0], todesc = results[1])
			f.write(html)

