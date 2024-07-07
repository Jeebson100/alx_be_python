# File: daily_reminder.py

def main():
    # Prompting user for input with specific prompts
    task = input("Enter your task: ")
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    priority = input("Priority (high/medium/low): ").strip().lower()

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

    # Printing the customized reminder
    print(f"Reminder:\n{reminder}")

if __name__ == "__main__":
    main()
