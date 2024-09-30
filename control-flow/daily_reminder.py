#Ask the user to input a task description and save it into a task variable
task = input("Enter your task: ")
#Prompt for the task’s priority (high, medium, low) and save it into a priority variable
priority = input("Priority (high/medium/low): ")
#In a time_bound variable, Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ")

#Use a Match Case statement to react differently based on the task’s priority.
#Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
#Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
#A message should be ‘that requires immediate attention today!’
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high-priority task that requires your attention.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium-priority task that needs to be completed soon.")
        else:
            print(f"Reminder: '{task}' is a medium-priority task. Put it on your to-do list.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low-priority task, but you should make some time for it.")
        else:
            print(f"Reminder: '{task}' is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid choice. Please select a valid priority (high/medium/low).")

