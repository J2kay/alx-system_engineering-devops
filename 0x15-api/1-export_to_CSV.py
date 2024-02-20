#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get("username")

    todosUrl = url + "/todos"
    response = requests.get(todosUrl)
    all_tasks = response.json()

    with open("{}.csv".format(employeeId), "w") as file:
        for task in all_tasks:
            file.write(
                '"{}","{}","{}","{}"\n'.format(
                    employeeId, username, task.get("completed"),
                    task.get("title")
                )
            )
