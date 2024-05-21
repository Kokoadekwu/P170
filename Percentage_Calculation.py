from tkinter import *

root = Tk()
root.title("Grade Percentage Calculator")
root.geometry("400x200")

class Grade3:
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        grade_percentage = (total_marks / 200) * 100
        return grade_percentage

class Grade5:
    def __init__(self, language_arts, mathematics, social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        grade_percentage = (total_marks / 300) * 100
        return grade_percentage

class Grade10:
    def __init__(self, language_arts, mathematics, social_studies, foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.foreign_language
        grade_percentage = (total_marks / 400) * 100
        return grade_percentage

    def calculate_grade_3_percentage():
        grade_3_obj = Grade3(85, 90)  # Example marks for Grade 3
        percentage = grade_3_obj.percentage()
        grade_3_label.config(text=f"Grade 3 Percentage: {percentage:.2f}%")

    def calculate_grade_5_percentage():
        grade_5_obj = Grade5(85, 90, 80)  # Example marks for Grade 5
        percentage = grade_5_obj.percentage()
        grade_5_label.config(text=f"Grade 5 Percentage: {percentage:.2f}%")

    def calculate_grade_10_percentage():
        grade_10_obj = Grade10(85, 90, 80, 75)  # Example marks for Grade 10
        percentage = grade_10_obj.percentage()
    grade_10_label.config(text=f"Grade 10 Percentage: {percentage:.2f}%")

grade_3_label = Label(root, text="")
grade_3_label.pack()

grade_5_label = Label(root, text="")
grade_5_label.pack()

grade_10_label = Label(root, text="")
grade_10_label.pack()

grade_3_button = Button(root, text="Grade 3", command=calculate_grade_3_percentage)
grade_3_button.pack()

grade_5_button = Button(root, text="Grade 5", command=calculate_grade_5_percentage)
grade_5_button.pack()

grade_10_button = Button(root, text="Grade 10", command=calculate_grade_10_percentage)
grade_10_button.pack()

root.mainloop()