import requests
import random
import time

# Your Discord Bot Token
TOKEN = "MTA2NzQ0MTY3NDc5NzcxNTUyNg.GCtyDM.soRrgAn5V47HXmU_TJUQNz8YkGvRga3WYr5K8k"
CHANNEL_ID = "1027161980970205225"

# Messages List
messages = [
    "Whales already loading up!",
    "One mint, life-changing gains!",
    "This gonna shake the space!",
    "The next blue-chip in the making!",
    "Community-powered rocket ship!",
    "WL spots disappearing fast!",
    "Big players watching closely!",
    "Future legends minting soon!",
    "We making history together!",
    "The grind never stops!",
    "Just wait till the FOMO kicks in!",
    "This mint gonna sell out instantly!",
    "Sleepless nights, priceless gains!",
    "No weak hands in this one!",
    "Every second counts!",
    "Building a legacy, not just hype!",
    "This project gonna dominate!",
    "We early, but not for long!",
    "You either in or you watching!",
    "Minting one? Nah, minting as many as possible!",
    "When roadmap execution is flawless!",
    "The hype train has no brakes!",
    "This floor won’t stay low for long!",
    "Who’s got their mint strategy ready?",
    "Straight to the top, no detours!",
    "The NFT world ain’t ready for this!",
    "Devs overdelivering as always!",
    "Market waking up to this gem!",
    "Can already smell the ATH coming!",
    "Holding strong, only winners here!",
    "Who’s minting and who’s watching from the sidelines?",
    "This is how generational wealth is made!",
    "Strong conviction, stronger community!",
    "The team ain't playing around!",
    "If you know, you stacking!",
    "First mover advantage right here!",
    "History books gonna remember this!",
    "Legendary project in the making!",
    "We just getting started fr!",
    "This ain’t a game, this is the future!",
    "The best projects always start like this!",
    "Mint day gonna be a wild ride!",
    "Y’all better buckle up!",
    "This team got everything locked in!",
    "We flipping blue-chips soon!",
    "FOMO levels reaching max!",
    "Real ones holding till the top!",
    "The roadmap just keeps getting better!",
    "Ain’t no stopping this momentum!",
    "The biggest NFT wave is here!"
]

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"

while True:
    message = random.choice(messages)
    payload = {"content": message}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"✅ Message Sent: {message}")
        wait_time = random.randint(120, 150)
    elif response.status_code == 429:
        retry_after = response.json().get("retry_after", 60)
        print(f"⏳ Rate Limited! Sleeping for {retry_after} seconds...")
        wait_time = retry_after
    else:
        print(f"❌ Error {response.status_code}: {response.json()}")
        wait_time = random.randint(120, 150)

    if wait_time > 10:
        wait_time -= random.randint(1, 10)

    print(f"Sleeping for {wait_time} seconds...")
    time.sleep(wait_time)
