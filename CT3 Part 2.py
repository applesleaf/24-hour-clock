def calculate_alarm_time():
    # Ask the user for the current time in hours (24-hour format)
    current_time = int(input("Enter the current time (0-23): "))
    
    # Validate the current time input
    if current_time < 0 or current_time > 23:
        print("Invalid input. Please enter a time between 0 and 23.")
        return

    # Ask the user for the number of hours to wait for the alarm
    wait_hours = int(input("Enter the number of hours to wait for the alarm: "))
    
    # Calculate the time the alarm will go off
    alarm_time = (current_time + wait_hours) % 24

    # Output the time when the alarm will go off
    print(f"The time when the alarm will go off is: {alarm_time}:00")

# Run the program
calculate_alarm_time()
