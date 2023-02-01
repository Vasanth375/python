import datetime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Patient:
    def __init__(self, name, admission_date, disease, discharge_date):
        self.name = name
        self.admission_date = admission_date
        self.disease = disease
        self.discharge_date = discharge_date
        
    def enter_info(self, name, admission_date, disease, discharge_date):
        self.name = name
        self.admission_date = admission_date
        self.disease = disease
        self.discharge_date = discharge_date
        
    def display_list(self):
        print("Name:", self.name)
        print("Admission Date:", self.admission_date.year, self.admission_date.month, self.admission_date.day)
        print("Disease:", self.disease)
        print("Discharge Date:", self.discharge_date.year, self.discharge_date.month, self.discharge_date.day)


class PatientWithAge(Patient):
    def __init__(self, name, admission_date, disease, discharge_date, age):
        super().__init__(name, admission_date, disease, discharge_date)
        self.age = age
        
    def enter_info(self, name, admission_date, disease, discharge_date, age):
        super().enter_info(name, admission_date, disease, discharge_date)
        self.age = age
        
    def display_list(self):
        super().display_list()
        print("Age:", self.age)

s = PatientWithAge("John Doe", Date(2020, 1, 1), "Fever", Date(2020, 1, 5), 10)
s.display_list()
