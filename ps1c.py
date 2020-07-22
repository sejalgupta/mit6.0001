#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:58:42 2020

@author: sgupta
"""

annual_salary = float(input('Enter the starting salary: ')) 
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = .25 * total_cost
count = 0
low = 0
high = 10000
val = True

while val:
    current_savings = 0
    salary = annual_salary
    percentSaved = (low + high)/2
    
    if low == high:
        print('It is not possible to pay the down payment in three years.')
        val = False
    
    for i in range(0, 36):
        current_savings += current_savings * .04/12 + salary/12 * percentSaved/10000
        if i % 6 == 0:
            salary += salary * semi_annual_raise
    print(current_savings)
    
    if ((abs(current_savings - portion_down_payment) <= 100)):
        print("Best savings rate: ", percentSaved/10000)
        print("Steps in bisection search: ", count)
        val = False
    
    if (current_savings - portion_down_payment > 100):
        high = percentSaved
    
    if (current_savings - portion_down_payment < -100):
        low = percentSaved
        
    
    count += 1
