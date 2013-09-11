#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: gpa.py
Author: huxuan
Email: i(at)huxuan.org
Description: Python Script to calculate the GPA
"""

FILE_PATH = 'gpa.txt'

def main():
    """docstring for main"""
    tot_credit_gpa = 0 # 学分绩点和
    tot_credit = 0 # 学分和

    with open(FILE_PATH) as file_gpa:
        for entry in file_gpa.readlines():
            entry = entry.split()
            # print repr(entry)
            grade = int(entry[0]) # 成绩
            credit = int(entry[1]) # 学分
            gpa = 4 - ( 3.0 * ( 100.0 - grade ) * ( 100.0 - grade ) / 1600.0 )
            if gpa < 1:
                gpa = 0
            # print grade, credit, gpa
            tot_credit += credit
            tot_credit_gpa += credit * gpa

    GPA = tot_credit_gpa / tot_credit # 总的GPA
    G = ( GPA - 1 ) * 25 # 用于学生素质综合测评的学习成绩

    print 'GPA =', GPA
    print 'G =', G

if __name__ == '__main__':
    main()
