
#__________________| SCRIPT INFO |__________________#
# SCRIPT MAKED BY BLACK MAFIA TEAM
# PYTHON VERSION : 3.5
# TELEGRAM : BLACK MAFIA 
# TEAM : BLACK MAFIA 
#_______________| IMPORT MODULES |________________#

import os
import random
import time

def clear():
    os.system("clear")

def banner():
    clear()
    print("\033[1;32m")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("       🌿 FB GRAPH + USER-AGENT TOOL 🌿")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   Developer: ●▬▬▬▬๑۩🇸‌🇭‌🇦‌🇱‌🇱‌🇴‌🇨‌🇰‌۩๑▬▬▬▬๑۩🇦‌🇩‌🇲‌🇮‌🇳‌◇🇴‌🇫‌◇🇧‌🇱‌🇦‌🇨‌🇰‌◇🇲‌🇦‌🇫‌🇮‌🇦‌◇۩๑▬▬▬▬●    ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

def menu():
    banner()
    print("1️⃣  Generate Facebook Graph API Headers")
    print("2️⃣  Generate Unlimited User-Agents")
    print("0️⃣  Exit")
    return input("\n🟢 Select Option: ")

def generate_graph_headers():
    banner()
    headers = {
        'Host': 'graph.facebook.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; SM-{random.choice(['G610F','A107F','J610F','M205F'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,120)}.0.{random.randint(1000,4999)}.{random.randint(100,200)} Mobile Safari/537.36",
    }
    file_path = "/sdcard/Download/graph_headers.txt"
    with open(file_path, "a") as f:
        f.write(str(headers) + "\n")
    print(f"\n✅ Header saved to: {file_path}")
    input("\n🔙 Press Enter to go back...")

def generate_user_agents():
    banner()
    try:
        limit = int(input("🔢 ENTER LIMIT? "))
        file_path = "/sdcard/Download/user_agents.txt"
        with open(file_path, "a") as f:
            for _ in range(limit):
                ua = f"Mozilla/5.0 (Linux; Android {random.randint(8,14)}; SM-{random.choice(['A107F','J610F','M205F','A125F','G610F'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,122)}.0.{random.randint(1000,4999)}.{random.randint(100,200)} Mobile Safari/537.36"
                f.write(ua + "\n")
        print(f"\n✅ {limit} User-Agents saved to: {file_path}")
    except:
        print("\n❌ Invalid input.")
    input("\n🔙 Press Enter to go back...")

while True:
    choice = menu()
    if choice == "1":
        generate_graph_headers()
    elif choice == "2":
        generate_user_agents()
    elif choice == "0":
        print("\n👋 Exiting... Thank you!")
        break
    else:
        print("\n❌ Invalid choice, try again!")
        time.sleep(1)
