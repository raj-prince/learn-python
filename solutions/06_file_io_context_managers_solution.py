#!/usr/bin/env python3
"""
================================================================================
LESSON 6: FILE I/O AND CONTEXT MANAGERS — SOLUTION
================================================================================
"""
import json

servers_data = [
    {"name": "Web-Server-01", "ip": "192.168.1.1", "status": "online"},
    {"name": "DB-Server-Primary", "ip": "192.168.1.2", "status": "offline"},
    {"name": "Cache-Node-A", "ip": "192.168.1.3", "status": "online"},
    {"name": "Auth-Gateway", "ip": "192.168.1.4", "status": "offline"},
    {"name": "Backup-Vault", "ip": "192.168.1.5", "status": "offline"}
]

# 1. Write the servers_data structure to servers.json
with open("servers.json", "w") as f:
    json.dump(servers_data, f, indent=4)
    print("✅ Created servers.json with server configurations.")

# 2. Read servers.json back into the program
with open("servers.json", "r") as f:
    loaded_servers = json.load(f)

# 3. Filter for offline servers
offline_servers = []
for server in loaded_servers:
    if server["status"] == "offline":
        offline_servers.append(server["name"])

# 4. Write the names of all offline servers into offline_report.txt
with open("offline_report.txt", "w") as report_file:
    for server_name in offline_servers:
        report_file.write(f"{server_name}\n")
    print("✅ Generated offline_report.txt with offline server names.")


# --- TEST CODE ---
print("\n--- Verifying Offline Report ---")
try:
    with open("offline_report.txt", "r") as report:
        lines = report.readlines()
        print("Offline servers found in report:")
        for line in lines:
            print(f"  - {line.strip()}")
        
        # Quick validation
        expected = ["DB-Server-Primary", "Auth-Gateway", "Backup-Vault"]
        actual = [line.strip() for line in lines]
        if actual == expected:
            print("🎉 Success! The report is 100% correct.")
        else:
            print("⚠️ The report contents don't match the expected offline servers.")
except FileNotFoundError:
    print("❌ Error: offline_report.txt was not found. Make sure you write to this file!")
