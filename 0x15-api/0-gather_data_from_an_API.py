#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    emp_name = response.json().get('name')

    todosUrl = url + "/todos"
    response = requests.get(todosUrl)
    all_tasks = response.json()
    completed = 0
    completedTasks = []

    for task in all_tasks:
        if task.get('completed'):
            completedTasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, completed, len(all_tasks)))

    for task in completedTasks:
        print("\t {}".format(task.get('title')))
