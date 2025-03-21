import instaloader
import getpass
import os
import time
import random

# Prompt for Instagram login and target account
USERNAME = input("Enter your Instagram username: ")
PASSWORD = getpass.getpass("Enter your Instagram password: ")
TARGET_ACCOUNT = input("Enter the username of the account you want to track: ")

# Setup Instaloader and log in
L = instaloader.Instaloader()
L.login(USERNAME, PASSWORD)

# Add random delays to mimic human behavior
def human_delay(min_seconds=2, max_seconds=5):
    time.sleep(random.uniform(min_seconds, max_seconds))

# Load current followers for the target account
profile = instaloader.Profile.from_username(L.context, TARGET_ACCOUNT)
current_followers = set()

print(f"Fetching followers for {TARGET_ACCOUNT} slowly to avoid detection...")
for follower in profile.get_followers():
    current_followers.add(follower.username)
    human_delay(1, 3)  # delay between each follower to mimic human actions

# Load previous followers if they exist
data_file = "data/last_followers.txt"
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        old_followers = set(file.read().splitlines())
else:
    old_followers = set()

# Compare old and current followers
new_followers = current_followers - old_followers

# Display results
if new_followers:
    print("New followers since last check:")
    for user in new_followers:
        print(user)
else:
    print("No new followers found.")

# Save current followers for the next comparison
os.makedirs("data", exist_ok=True)
with open(data_file, "w") as file:
    for follower in current_followers:
        file.write(f"{follower}\n")
