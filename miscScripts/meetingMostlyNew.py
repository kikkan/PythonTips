import numpy as np
from datetime import datetime as dt
import os

#%%MARK: About
# Quick (bruteforce) script for setting up group meetings over several days
# while trying to make no two persons meet twice.

# Note: Can be made faster by considering persons with highest amount of 
# reacurring meetings first.

#%%MARK: Class
class Person():
    maxMet = 0

    def __init__(self, name):
        self.name = name
        self.met = {}
        self.personalMaxMet = 0

    def meeting(self, participants):
        self.currMeeting = participants.copy()
        for p in participants:
            if p.name != self.name:
                if p.name in self.met.keys():
                    self.met[p.name] += 1
                    if self.met[p.name] > self.personalMaxMet:
                        self.personalMaxMet = self.met[p.name]
                        if self.personalMaxMet > self.maxMet:
                            self.changeMaxMet(Person, self.met[p.name])
                else:
                    self.met[p.name] = 1

    def revert(self):
        for p in self.currMeeting:
            if p.name != self.name:
                self.met[p.name] -= 1
        i = 0
        for m in self.met.values():
            if m > i:
                i = m
        self.personalMaxMet = i

    def __repr__(self):
        return self.name

    @staticmethod
    def changeMaxMet(cls, i):
        cls.maxMet = i


# l = 7

# k2 = klasse.copy()
# meetings = {}
# for i in range(l):
#     meetings[i] = []

#%%MARK: Functions
def meet(participants, m):
    k2 = participants.copy()
    meetings = {}
    for i in range(m):
        meetings[i] = []

    while k2:
        for i in range(m):
            r = np.random.randint(0, len(k2))
            meetings[i].append(k2.pop(r))
            if len(k2) == 0:
                break

    return meetings


def meetingLeastReEncouneters(participants, tol, maxiter, n):
    req = False # Bolean for zero reacurring meetings(?)
    for i in range(maxiter):
        M = meet(participants, n)
        for mt in M.values():
            for p in mt:
                p.meeting(mt)
        if participants[0].maxMet <= tol:
            req = True
            break
        else:
            for p in participants:
                p.revert()
    return M, req


def findBestMeeting(participants, maxiter, days, groups):
    d = {}
    tol = 1
    for i in range(days):
        while True:
            d[i], req = meetingLeastReEncouneters(participants, tol, maxiter, groups)
            if req:
                break
            tol += 1
            if tol >= 100:
                print(tol)
    return d


#%%MARK: RUN 
path = os.path.dirname(__file__) # failsafe for running when root is not correct.
f = open(path + '\\Persons.txt', 'r')

klasse = []
for p in f.readlines():
    klasse.append(Person(p.strip()))

start = dt.now()
bestSetup = findBestMeeting(klasse, 100000, 4, 7)


for day, meetings in bestSetup.items():
    print('#'*10 + '\n' + f'Dag {day}')
    i = 1
    for meeting in meetings.values():
        print(f'Møte {i}')
        for p in meeting:
            print(p.name, end=', ')
        print('\n')
        i += 1
o = 0
for p in klasse:
    o += p.personalMaxMet
print(f'Average reacurring meetings: {o/len(klasse)}')
print(f'Max reacurring meetings: {klasse[0].maxMet}')

print(f'\nruntime: {dt.now() - start}')

print('{:<12}|{:^20}|{}'.format('navn', 'antall gjentagende', 'hvem'))
for p in klasse:
    if p.personalMaxMet > 1:
        navn = p.name
        meetMost = []
        for m, n in p.met.items():
            if n == p.personalMaxMet:
                meetMost.append(m)
        print('{:<12}|{:^20}|'.format(p.name, p.personalMaxMet), end='')
        print(meetMost)

print()
