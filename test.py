import csv

class Main:
	def csv_r(self, string):
		data_set = open(string, 'r')
		data_list = []
		
		for line in data_set:
			data_list.append(line)

		new_data_list = []
		for line in data_list:
			l = line.split(',')
			new_data_list.append(l)
			
		return new_data_list

	def main(self):
		data_set = self.csv_r('final.csv')
			
		for line in data_set:
			if line[0] == 'Loan_ID':
				continue
			if int(line[8])-(int(line[6])+int(line[7]))/1000 < 0:
				print('Yes')







main = Main()
main.main()
