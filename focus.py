import time
import sys
from plyer import notification
import platform
import os

def start_timer(minutes):
    total_seconds = minutes * 60

    print(f"Focus Timer started for {minutes} minutes.")
    print("Do not close this terminal window.\n")

    for i in range(total_seconds+1):
        remaining_time = total_seconds - i
        
        # split remaining time into minutes and seconds for display
        mins_left = remaining_time // 60
        seconds_left = remaining_time % 60

        width = 30
        percentage_completed = i/total_seconds
        filled_chars = int(width * percentage_completed)

        display_chars = '█' * filled_chars + '-' * (width - filled_chars)

        # update terminal
        sys.stdout.write(f"\r[{display_chars}] {mins_left:02d}:{seconds_left:02d} remaining")
        sys.stdout.flush()

        time.sleep(1)


    notification.notify(
        title='Pomodoro Timer',
        message='Time interval completed.',
        timeout=5
    )
    print("\nTimer completed.")
    play_sound()


    time.sleep(1)

def play_sound():
    system_name = platform.system()

    if system_name == "Windows":
        import winsound
        winsound.Beep(1000, 1000)
    
    elif system_name == "Darwin":
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    
    else:
        print('\a')

if __name__ == "__main__":
    try:
        user_input = input("Enter focus minutes (defaults to 25): ")

        if user_input.strip() == "":
            minutes = 25
        else:
            if int(user_input) > 99:
                user_input = int(99)
            minutes = int(user_input)
        
        start_timer(minutes)

    except KeyboardInterrupt:
        print("\nTimer stopped.")
    except ValueError:
        print("\nPlease enter a valid number.")