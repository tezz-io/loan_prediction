class App:
	def __init__(loan_id, gender, is_married, dependents, edu, is_self_employed, app_income, co_income, loan_amt, loan_term, credit_score, property, loan_approved):
		self.id = int(loan_id)
		self.gender = gender
		self.marriage = Married(is_married)
		self.dependents = Dependents(dependents)
		self.edu = Education(edu)
		self.self_emp = SelfEmployed(is_self_employed)
		self.app_income = ApplicantIncome(app_income)
		self.co_income = CoApplicantIncome(co_income)
		self.loan_amt = LoanAmount(loan_amt)
		self.loan_term = LoanTerm(loan_term)
		self.credit_score = CreditScore(credit_score)
		self.property = Property(property)
		self.loan_approved = LoanApproved(loan_approved)


class Married:
	def __init__(self, is_married):
		if is_married == 'Yes':
			self.value = 2
		else:
			self.value = 1


class Dependents: 
  def __init__(self, value):
  	if value == '3+':
  		self.value = 3
  	elif value == '2':
  		self.value == 2
  	elif value == '1':
  		self.value = 1
  	else:
  		self.value = 0


class Education:
	def __init__(self, s):
		if s == "Graduate":
			self.value = 4
		else:
			self.value = 1


class SelfEmployed:
	def __init__(self, b):
		if b == 'No':
			self.value = 2
		else:
			self.value = 1


class ApplicantIncome:
	def __init__(self, income):
		self.value = income


class CoApplicantIncome:
	def __init__(self, income):
		self.value = income


class LoanAmount:
	def __init__(self, amount):
		self.value = income


# class LoanTerm:
# 	def __init__(self, months):
# 		if months == '':
# 			elf.value = 120
# 		else:
# 			self.value = int(months)


# class CreditScore:
# 	def __init__(self, score):
# 		if score == '1':
# 			self.value = 1
# 		else:
# 			self.value = 0


# class Property:
# 	def __init__(self, status):
# 		if status == "Urban":
# 			self.value = 4
# 		elif status == "Semiurban":
# 			self.value = 2
# 		elif status == "Rural":
# 			self.value = 1
# 		else:
# 			self.value = 0


# class LoanApproved:
# 	def __init__(self, is_approved):
# 		if is_approved == 'Y':
# 			self.value = True
# 		else:
# 			self.value = False





















#   public static void main(String[] args) {
#     App[] a = new App[100];
#     double x1, x2, x3, x4, x5, x6, x7, x8, x9; 
#     // Note: x1 + x2 + x3 + ... + x8 + x9 = 100
#     //Initialize using data
#     for(All the data) {
#       //Do something according to some algotithm
#       a[i].result = x1*m.value + x2*d.value + x3*edu.value + x4*s.value + x5*ai.value + 
#              x6*cai.value + x7*la.value + x8*lt.value + x9*cs.value;
#     }
#     //From the algorithm, we will have mean values for x1 to x9;
#     //We will plugin values for x1 to x9 in a[i].result and get the threshold value
#     //for LoanApproved status=true  => (a[i].result > threshold)
#     //for LoanApproved status=false => (a[i].result < threshold)
#   } 
# }








import csv

train = open('train.csv', 'r')
mylines = csv.reader(train)

x = 0
n = 0
'''for myline in mylines:
	if myline[8] == 'LoanAmount':
		continue
	if myline[8] != '':
		x += int(myline[8])
		n += 1
'''
for myline in mylines:
	print(myline)

# print(x)
# print(x/n)

# final = open('final.txt', 'w+', newline='')
# writer = csv.writer(final)

# flines = []
# for myline in mylines:
# 	if myline[8] == 'LoanAmount':
# 		continue
# 	if myline[8] != '':
# 		l = []
# 		for i in range(0, 8):
# 			l.append(i)
# 		l.append('146')
# 		for i in range(9, len(myfile)):
# 			l.append(i)
# 		flines.append(l)
# 	else:
# 		flines.append(myline)	



# for i in flines:
# 	for s in i:
# 		final.write(s)
