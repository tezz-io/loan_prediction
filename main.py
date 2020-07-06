
class App:
	def __init__(self, loan_id, gender, is_married, dependents, edu, is_self_employed, app_income, co_income, loan_amt, loan_term, credit_score, propert, loan_approved):
		self.id = int(loan_id)
		self.gender = gender
		self.marriage = Married(is_married)
		self.dependents = Dependents(dependents)
		self.edu = Education(edu)
		self.self_emp = SelfEmployed(is_self_employed)
		self.app_income = ApplicantIncome(int(app_income))
		self.co_income = CoApplicantIncome(int(co_income))
		self.loan_amt = LoanAmount(int(loan_amt))
		self.loan_term = LoanTerm(loan_term)
		self.credit_score = CreditScore(credit_score)
		self.property = Property(propert)
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
		self.value = amount


class LoanTerm:
	def __init__(self, months):
		if months == '':
			self.value = 120
		else:
			self.value = int(months)


class CreditScore:
	def __init__(self, score):
		if score == '1':
			self.value = 1
		else:
			self.value = 0


class Property:
	def __init__(self, status):
		if status == "Urban":
			self.value = 4
		elif status == "Semiurban":
			self.value = 2
		elif status == "Rural":
			self.value = 1
		else:
			self.value = 0


class LoanApproved:
	def __init__(self, is_approved):
		if is_approved == 'Y':
			self.value = True
		else:
			self.value = False

