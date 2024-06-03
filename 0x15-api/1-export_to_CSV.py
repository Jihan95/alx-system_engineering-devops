#!/usr/bin/python3
""" using this a url, for a given employee ID,returns information about his/her
TODO list progress. and save information into csv file """


import csv
import requests
import sys


def main():
    """ main function """
    if sys.argv[1]:
        fixed = 'https://jsonplaceholder.typicode.com/'
        url = fixed + 'todos/?userId=' + sys.argv[1]
        url1 = fixed + 'users/?id=' + sys.argv[1]
        response = requests.get(url)
        emp_name = requests.get(url1).json()[0]["username"]
        if response.status_code == 200:
            data = response.json()
            with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for i in data:
                    row = [sys.argv[1], emp_name, i['completed'], i['title']]
                    writer.writerow(row)
    else:
        print('USAGE: 1-export_to_CSV.py EMPLOYEE_ID')


if __name__ == "__main__":
    main()
