import os
import datetime
import time

def schedule_shutdown():
    # Define start time
    start_time = datetime.datetime.now().replace(hour=4, minute=0, second=0, microsecond=0)

    # Define shutdown time for the next day
    shutdown_time = start_time

    while shutdown_time.hour < 21:  # Continue until 9:00 PM
        # Calculate shutdown time 30 minutes earlier
        shutdown_time = shutdown_time + datetime.timedelta(minutes=-30)

        # Wait until the scheduled shutdown time
        current_time = datetime.datetime.now()
        time_difference = (shutdown_time - current_time).total_seconds()

        if time_difference > 0:
            print(f"Waiting for {int(time_difference / 60)} minutes until the next shutdown...")
            time.sleep(time_difference)
        
        # Execute shutdown command
        os.system("shutdown /s /t 1")

if __name__ == "__main__":
    schedule_shutdown()