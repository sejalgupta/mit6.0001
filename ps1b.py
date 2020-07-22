#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:58:42 2020

@author: sgupta
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))

portion_down_payment = .25 #25% of the total_cost needs to be given
current_savings = 0

def monthlyReturn(savings):
    '''
    Parameters
    ----------
    savings : float
        the current savings of the individual.

    Returns
    -------
    float
        monthly return of current savings.

    '''
    r = .04
    return savings*r/12

def monthlySalaryPercentage():
    '''
    Returns
    -------
    float
        percentage of monthly salary saved for the house
    '''
    monthly_salary = annual_salary/12
    return monthly_salary * portion_saved

def annualRaise():
    '''
    Returns
    -------
    float
        raise amount
    '''
    return annual_salary * semi_annual_raise

numberMonths = 0

while (current_savings < (portion_down_payment * total_cost)):
    #adds the monthly return and monthly portion of the salary to the savings
    current_savings = current_savings + monthlyReturn(current_savings) + monthlySalaryPercentage()
    numberMonths += 1
    if numberMonths % 6 == 0:
        annual_salary += annualRaise()
    
print("Number of months:", numberMonths)