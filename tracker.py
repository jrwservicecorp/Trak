import instaloader
import os
import time
import random

# Your login and target account
USERNAME = "your_ig_username"
PASSWORD = "your_ig_password"
TARGET_ACCOUNT = "target_account_username"

# Initialize and log in
L = instaloader.Instaloader()
L.login(USERNAME, PASSWORD)

# Add random delays to mimic human behavior
def human_delay(min_seconds=2, max_seconds=5):
    time.sleep(random.uniform(min_seconds, max_seconds))

# Get followers for the target account
profile = instaloader.Profile.from_username(L.context, TARGET_ACCOUNT)
current_followers = set()

print(f"Fetching followers for {TARGET_ACCOUNT} slowly to avoid detection...")
for follower in profile.get_followers():
    current_followers.add(follower.username)
    human_delay(1, 3)

# Compare to last run
data_file = "data/last_followers.txt"
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        old_followers = set(file.read().splitlines())
else:
    old_followers = set()

new_followers = current_followers - old_followers

# Display results
if new_followers:
    print("New followers since last check:")
    for user in new_followers:
        print(user)
else:
    print("No new followers found.")

# Save for next run
os.makedirs("data", exist_ok=True)
with open(data_file, "w") as file:
    for follower in current_followers:
        file.write(f"{follower}\n")

