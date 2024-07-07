# File: daily_reminder.py

def main():
    # Prompting user for input
    task = input("Enter the task description: ")
    priority = input("Enter the priority level (high/medium/low): ").strip().lower()
    time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

    # Processing the task based on priority and time sensitivity
    match priority:
        case 'high':
            reminder = f"Task '{task}' is of HIGH priority."
        case 'medium':
            reminder = f"Task '{task}' is of MEDIUM priority."
        case 'low':
            reminder = f"Task '{task}' is of LOW priority."
        case _:
            print(f"Invalid priority level '{priority}'. Please choose high, medium, or low.")
            return

    if time_bound == 'yes':
        reminder += " This task requires immediate attention today!"

    # Providing the customized reminder
    print(reminder)

if __name__ == "__main__":
    main()
