#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 chris <chris@home>
#
# Distributed under terms of the MIT license.

"""
Contains task object definition, this object isn't
very useful at the moment
"""
import re
from datetime import datetime

class Task:
    def __init__(
    self,                   \
    complete=False,         \
    priority=str(),         \
    completion_date=None,   \
    creation_date=None,       \
    description=[],         \
    tags={},                \
    contexts=[],            \
    projects=[]             \
    ):
        self.complete = False
        self.priority = str()
        self.completion_date = None
        self.creation_date = None
        self.description = []
        self.tags = {}     # Map strings to strings
        self.contexts = []  # IE '@GPIO'
        self.projects = [] # IE: +RPi

    def list(self):
        return self.description

    def __str__(self):
        return " ".join(self.description)

    def _init_failed(self):
        print("Malformed todo item, required context/project/description tags missing")
        return self

    # We compare description lists only
    def __eq__(self, other):
        if not other or not self:
            return False
        return \
        (self.description == other.description)

    """
    Tasks are saved in todo.txt format,
    each line of a todo.txt format will represent a task.
    The format of the line is:
    [Optional priority] [Optional creation date] [everything else,]
    """
    def init_todo_txt(line):
        list_line = line.split(' ')
        return Task._list_init(list_line)

    def _list_init(list_line):
        todo_priority = "\([A-Z]\)"
        todo_dt_fmt = "%Y-%m-%d"
        todo_dt_regex = "\d\d\d\d-\d\d-\d\d"
        start = 0
        task = Task()
        task.description = list_line
        # Check completion
        if list_line[0][0] == 'x':
            task.complete = True
            start += 1
            if start > len(list_line):
                return task._init_failed()
            # TODO: Check completion date
        # Check priority
        match = re.fullmatch(todo_priority, list_line[start])
        if match:
            task.priority = list_line[start]
            start += 1
            if start > len(list_line):
                return task._init_failed()
        # Check creation date
        match = re.fullmatch(todo_dt_regex, list_line[start])
        if match:
            task.creation_date = datetime.strptime(list_line[start], todo_dt_fmt)
            start += 1
            if start > len(list_line):
                return task._init_failed()
        # Check the rest
        for i in range(start,len(list_line)):
            match = re.fullmatch(todo_dt_regex, list_line[i])
            if match: pass
                #task.completion_date = datetime.strptime(list_line[i], todo_dt_fmt)
            elif list_line[i][0] == '+':
                task.projects.append(list_line[i])
            elif list_line[i][0] == '@':
                task.contexts.append(list_line[i])
        return task
