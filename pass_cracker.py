# Password Cracker to try and crack the passwords that your Password Generator creates

import itertools
import string
import time
def calculate_combinations(charset_length, max_password_length):
    return sum(charset_length ** i for i in range(1, max_password_length + 1))

def estimate_cracking_time(combinations, attempts_per_second):
    seconds = combinations / attempts_per_second
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds

def display_time(days, hours, minutes, seconds):
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds"

def brute_force_crack(target_password, charset):
    attempts = 0
    for password_length in range(1, len(target_password) + 1):
        for guess in itertools.product(charset, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                return (guess, attempts)
    return (None, attempts)

# Define character set and target password
charset = string.ascii_letters + string.digits
#target = "9q{Nx/x(!]!eZt"
target = input("Enter Password to Crack: ")


# Assume a speed of attempts per second
attempts_per_second = 1000000  # Adjust based on your system's performance

# Calculate combinations and estimate time
combinations = calculate_combinations(len(charset), len(target))
estimated_days, estimated_hours, estimated_minutes, estimated_seconds = estimate_cracking_time(combinations, attempts_per_second)

print(f"Estimated maximum time to crack the password: {display_time(estimated_days, estimated_hours, estimated_minutes, estimated_seconds)}")

# Ask user if they want to proceed
user_input = input("Do you want to attempt to crack the password? (yes/no): ").strip().lower()

if user_input == "yes":
    start_time = time.time()
    cracked_password, attempts = brute_force_crack(target, charset)
    end_time = time.time()
    
    if cracked_password:
        print(f"Password cracked: {cracked_password} in {attempts} attempts and took {end_time - start_time:.2f} seconds.")
    else:
        print("Password not cracked.")
else:
    print("Cracking attempt aborted by the user.")
