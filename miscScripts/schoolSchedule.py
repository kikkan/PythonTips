import numpy as np

#%%MARK: About
#!  Unfinished
# Script to make optimal school class schedule.

class Course():
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.hoursLeft = hours
        self.teachers = []
        self.cantOverlap = []

    def setTeachers(self, teacher):
        self.teachers.append(teacher)

    def setTime(self, tFrom, tTo):
        if tTo <= tFrom:
            raise ValueError("Starttime must be before endtime.")

        if self.hoursLeft - (tTo - tFrom) > 0:
            self.hoursLeft -= tTo - tFrom
            # Perhaps come with suggestion if condition is not satisfied?

    def setOverlap(self, course):
        self.cantOverlap.append(course)

    def __add__(self, course):
        for teacher in self.teachers:
            for oTeacher in course.teachers:
                if teacher == oTeacher:
                    self.setOverlap(course)
                    course.setOverlap(self)


class Schedule():
    def __init__(self, year):
        self.year = year
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)
