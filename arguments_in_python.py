# -*- coding: utf-8 -*-
"""arguments in python



#ARGUMENT
#keyword argument
def students (name, branch, year, score):
   print("name:", name)
   print("branch:", branch)
   print("year:", year)
   print("score:", score)
students(name = "anjali", branch = "CSE", year = 2020, score = 90)
students("sahithi", "MCA", 2019, 80)

#defualty argument
def student(name , branch, year , score = 90):
   print("name :", name )
   print("branch:", branch)
   print("year:", year)
   print("score:", score)
student(name = "anjali", branch = "MCA", year = 2020)

#multiplr items
def student(branch , year , *name, score= 90):
      print("branch:", branch)
      print("year:", year)
      print("name :", name)
      print("score:", score)
student("mca", 2026, "anjali", "sahithi")
