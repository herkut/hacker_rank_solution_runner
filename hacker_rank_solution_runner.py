#!/usr/bin/python
import sys
from subprocess import run, PIPE


def main():
	if len(sys.argv) != 4:
		print("Unexpected argumensts")
		print(sys.argv)
		exit(1)
		
	command = sys.argv[1]
	input_file = sys.argv[2]
	expected_output_file = sys.argv[3]
	
	input_str_raw = ''
	with open(input_file) as f:
		input_str_raw = f.readlines()

	expected_outputs = ''
	with open(expected_output_file) as f:
		expected_outputs = f.readlines()

	input_str = ''
	for tmp_str in input_str_raw:
		input_str += tmp_str

	p = run(command, stdout=PIPE, input=input_str, encoding='ascii', shell=True)

	your_solution_outputs = p.stdout.split('\n')

	your_solution_outputs = your_solution_outputs[:-1]

	your_solution_outputs = [item.strip() for item in your_solution_outputs]

	expected_outputs = [item.strip() for item in expected_outputs]

	if len(expected_outputs) != len(your_solution_outputs):
		print('Expected outputs have ' + str(len(expected_outputs)) + ' results')
		print('Your solution outputs have ' + str(len(your_solution_outputs)) + ' results')
		exit(1)

	found_any_erroneous_result = False
	for i in range(len(expected_outputs)):
		if expected_outputs[i] != your_solution_outputs[i]:
			found_any_erroneous_result = True
			print(str(i) + 'th output is different')
			print('In expected output: ' + expected_outputs[i] + ' in your solution: ' + your_solution_outputs[i])

	if not found_any_erroneous_result:
		print('Congratulations, your solution is ok!')
		exit(0)
	else:
		exit(1)


if __name__ == '__main__':
	main()
