from sys import argv

global d_letters
d_letters = {}

def calc_c(f_file):
	for c in f_file.read(): 
		if not d_letters.__contains__(c):
			d_letters[c] = 1
		else:
			d_letters[c] += 1
	return d_letters

def main():
	calc_c(open(argv[1], 'r'))
	
	
	

if __name__ == '__main__':
	main()
