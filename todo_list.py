#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:20:28 2025

@author: lyss
"""

tasks = [] # empty list of tasks

while True:
    print("\nTo-Do List Menu:")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task description: ")
        tasks.add({'task': task, 'completed': False})
        print(f'Task "{task}" added.')

    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            for i in range(len(tasks)):
                status = "Done" if tasks[i]['completed'] else "Pending"
                print(f"{i + 1}. {tasks[i]['task']} - {status}")

    elif choice == '3':
        task_number = int(input("Enter the task number to mark as completed: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f'Task "{tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    elif choice == '4':
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
