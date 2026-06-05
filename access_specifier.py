# -*- coding: utf-8 -*-
"""Access specifier
# ACCESS SPECIFIERS
class student:
  def __init__(self, name , branch, score, result):
       self. name = name
       self._branch = branch
       self.__score = score
       self.__result = result
  def showname(self):
       print(self.name)
  def _showbranch(self):
       print(self._branch)
  def _showscore(self):
       print(self.__score)
  def _showresult(self):
      print(self.__result)
a = student("anjali", "MCA", 90, "passed")
a.showname()
a._showbranch()
a._showscore()
a._showresult()
