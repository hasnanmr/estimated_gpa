import pandas as pd
from termcolor import colored


class Transcript:
    
    def __init__(self, name, study):
        self.transcript = dict()
        self.name = name
        self.study = study
        
    def input_item(self):
        # show the error from input_item method
        try:
            # Looping the input while True, break with yes or no condition
            while True:
                course = input("Input the course name : ").title()  # user input for items as keys in dict
                alphabet = input(
                    "Input the value of alphabet of the course : ").upper()  # user input for quantity as values in dict
                credit = int(input(
                    "Input the credit of the course : ").strip())  # user input for price as values in dict
                # check whether keys in dict of self.transaction or not
                if course in self.transcript:
                    # if keys in dict of self.transaction will be executed print
                    print(colored(
                        "\nError! Item already in your order, try to input another items".upper(), "red"))
                # if keys not in dict of slf.transaction will be input as new keys and values in dict
                else:
                    self.transcript[course] = [alphabet, credit]
                    condition = input(
                        "Do you want to input another courses?(y/n): ").lower()  # break condition "y" or "n"
                    if condition == "n":  # will be printed cart in dataframe and break the method
                        print(colored
                              ("\nYour courses have been successfully added!\n".upper(), "green"))
                        break
                    elif condition == "y":
                        continue
                    else:
                        print(colored("wrong input! please input y or n".upper(), "red"))
                        print(colored("\nchoose the add item to input more courses\n".upper(), "green"))
                        break
        except ValueError:
            print('You should input as in the instruction')
        except NameError:
            print('only input with number from option')
        except SyntaxError:
            print('wrong syntax') 
            
    def show_transcript(self):
        df = pd.DataFrame.from_dict(self.transcript, orient='index', columns=['Index', 'Credit'])
        print(df.rename_axis('Courses').to_markdown())

    def total_index(self):
        
        self.show_transcript()
        
        index_total = 0  # express the index with zero
        
        #  Looping the process
        for key in self.transcript.keys():
            if self.transcript[key][0] == "A":
                index_total = index_total + (4 * self.transcript[key][1])
            elif self.transcript[key][0] == "B+":
                index_total = index_total + (3.5 * self.transcript[key][1])
            elif self.transcript[key][0] == "B":
                index_total = index_total + (3 * self.transcript[key][1])
            elif self.transcript[key][0] == "C+":
                index_total = index_total + (2.5 * self.transcript[key][1])
            elif self.transcript[key][0] == "C":
                index_total = index_total + (2 * self.transcript[key][1])
            elif self.transcript[key][0] == "D+":
                index_total = index_total + (1.5 * self.transcript[key][1])
            elif self.transcript[key][0] == "D":
                index_total = index_total + (1 * self.transcript[key][1])
            elif self.transcript[key][0] == "E":
                index_total = index_total + (0 * self.transcript[key][1])

        return index_total
    
    def total_credit(self):
        
        credit_total = 0  # express the credit with zero
        
        for key in self.transcript.keys():
            credit_total = credit_total + self.transcript[key][1]
            
        return credit_total
    
    def calculate_gpa(self):
        
        total_gpa = round(self.total_index() / self.total_credit(), 2)
        
        print(colored(
            f"\n{self.name}, student of {self.study} have got {total_gpa} in this semester".title(), "green"))
        
        return total_gpa
    
    def possible_gpa(self, future_credit, target):
        
        future_gpa = round(
            ((target * (future_credit + self.total_credit())) - (self.total_credit() * self.calculate_gpa())) / future_credit, 2)
        
        print(colored(f"{self.name},you have to reach {future_gpa} in next semester so you'll have GPA of {target}".upper(),
              "green"))
        
        return future_gpa

    def update_item(self):

        # Looping the input while True, break with yes or no condition
        while True:
            print("Choose from this option\n1. Courses\n2. Index Alphabet\n3. Credits\n  Write the number on input below!\n")
            condition = int(input("What do you want to update from your transcript: "))
            if condition == 1:
                course_name = input("Input the course you want to change: ").title()
                if course_name in self.transcript:
                    new_course = input("Input the new course to be updated: ").title()
                    self.transcript[new_course] = self.transcript.pop(course_name)
                else:
                    print(colored("Course(s) is/are not found".upper(), "red"))
            elif condition == 2:
                course_name = input("Input the course which you want to change the index: ").title()
                if course_name in self.transcript:
                    index_new = (input("Input the new index to be updated: ").strip())
                    credit = self.transcript[course_name][1]
                    self.transcript[course_name] = [index_new, credit]
                else:
                    print(colored("Course(s) is/are not found".upper(), "red"))
            elif condition == 3:
                course_name = input("Input the course which you want to change the credit: ").title()
                if course_name in self.transcript:
                    new_credit = int(input("Input the new credit to be updated: ").strip())
                    index = self.transcript[course_name][0]
                    self.transcript[course_name] = [index, new_credit]
                else:
                    print(colored("Course(s) is/are not found".upper(), "red"))
            else:
                print(colored("Invalid, please choose some numbers from the first sentence!", "red"))
            condition_2 = input("Do you still want to update? (y/n): ")
            if condition_2 == "n":
                print(colored("\nYour transcript is now updated!\n".title(), "green"))
                break
            else:
                continue


student_1 = Transcript('Ais', 'japanese literature')
student_1.input_item()
student_1.total_credit()
student_1.total_index()
student_1.calculate_gpa()
student_1.possible_gpa(24, 3.95)