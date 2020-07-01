public class App {
  int loan_id;
  Married m;
  Dependents d;
  Education edu;
  SelfEmployed s;
  ApplicantIncome ai;
  CoApplicantIncome cai;
  LoanAmount la;
  LoanTerm lt;
  CreditScore cs;
  double result;
  LoanApproved status;

  public static void main(String[] args) {
    App[] a = new App[100];
    double x1, x2, x3, x4, x5, x6, x7, x8, x9; 
    // Note: x1 + x2 + x3 + ... + x8 + x9 = 100
    //Initialize using data
    for(All the data) {
      //Do something according to some algotithm
      a[i].result = x1*m.value + x2*d.value + x3*edu.value + x4*s.value + x5*ai.value + 
             x6*cai.value + x7*la.value + x8*lt.value + x9*cs.value;
    }
    //From the algorithm, we will have mean values for x1 to x9;
    //We will plugin values for x1 to x9 in a[i].result and get the threshold value
    //for LoanApproved status=true  => (a[i].result > threshold)
    //for LoanApproved status=false => (a[i].result < threshold)
  } 
}

class Married {
  int value;
  Married(boolean b) {
    if(b)
      value = 1;
    else
      value = 0;
  }
}

class Dependents {
  int value;
  Dependents(int value) {
    this.value = value;
  }
}

class Education {
  int value;
  Education(String s) {
    if(s.toUpper() == "HS")
      value = 0;
    else if(s.toUpper() == "UG")
      value = 1;
    else if(s.toUpper() == "G")
      value = 2; 
  }
}

class SelfEmployed {
  int value;
  SelfEmployed(boolean b) {
    if(b) 
      value = 1;
    else
      value = 2;
  }
}

class ApplicantIncome {
  int value;
  ApplicantIncome(float income) {
    value = income / 100;
  }
}

class CoApplicantIncome {
  int value;
  CoApplicantIncome(float income) {
    value = income / 200;
  }
}

class LoanAmount {
  int value;
  LoanAmount(float amt) {
    value = amt / 100;
  }
}

class LoanTerm {
  int value;
  LoanTerm(int months) {
    value = months;
  }
}

class CreditScore {
  int value;
  CreditScore(int score) {
    value = score;
  }
}

class LoanApproved {
  boolean value;
}
