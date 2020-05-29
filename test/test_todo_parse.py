#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 chris <chris@home>
#
# Distributed under terms of the MIT license.

"""
Unit testing module for todo_txt support
functions

example todo.txt files are provided in
this directory
"""
from TimeTracker.task import Task
from datetime import datetime

todo_dt_fmt = "%Y-%m-%d"
# Example object delcarations
#x completed @test +todo
A = Task()
A.complete = True
A.priority = str()
A.due_date = None
A.create_date = None
A.description = "x completed @test +todo".split(" ")
A.tags = {}
A.contexts = ['@test']
A.projects = ['+todo']

#(A) 2019-11-20 due soon
B = Task()
B.complete = False
B.priority = "(A)"
B.due_date = None
B.create_date = datetime.strptime("2019-11-20",todo_dt_fmt)
B.description = "(A) 2019-11-20 due soon".split(" ")
B.tags = {}
B.contexts = []
B.projects = []

def test_task_init_A():
    line = "x completed @test +todo"
    task = Task.init_todo_txt(line)
    assert task == A

def test_task_init_B():
    line = "(A) 2019-11-20 due soon"
    task = Task.init_todo_txt(line)
    assert task == B
