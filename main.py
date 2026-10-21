import time
import platform

logs = []
cpu = 35
ram = 48
disk = 62

print("=" * 45)
print("SYSTEM MONITOR v1.0")
print("=" * 45)
print("Starting system...")
time.sleep(1)
print("System started!")

while True:
    print("\n" + "=" * 45)
    print("SYSTEM MONITOR")
    print("=" * 45)
    print("1. System information")
    print("2. Check CPU")
    print("3. Check RAM")
    print("4. Check disk")
    print("5. Change CPU usage")
    print("6. Change RAM usage")
    print("7. Change disk usage")
    print("8. Show logs")
    print("9. Full system status")
    print("10. Exit")
    choice = input("\nSelect option: ")

    if choice == "1":
        print("\n--- SYSTEM INFO ---")
        print("OS:", platform.system())
        print("Version:", platform.release())
        print("Computer:", platform.node())
        print("Processor:", platform.processor())
        logs.append("System information checked")

    elif choice == "2":
        print("\n--- CPU STATUS ---")
        print("CPU usage:", cpu, "%")
        if cpu < 60:
            print("Status: NORMAL")
        elif cpu < 85:
            print("Status: HIGH")
        else:
            print("Status: CRITICAL")
        logs.append("CPU checked")

    elif choice == "3":
        print("\n--- RAM STATUS ---")
        print("RAM usage:", ram, "%")
        if ram < 70:
            print("Status: NORMAL")
        elif ram < 90:
            print("Status: HIGH")
        else:
            print("Status: CRITICAL")
        logs.append("RAM checked")

    elif choice == "4":
        print("\n--- DISK STATUS ---")
        print("Disk usage:", disk, "%")
        if disk < 70:
            print("Status: NORMAL")
        elif disk < 90:
            print("Status: WARNING")
        else:
            print("Status: CRITICAL")
        logs.append("Disk checked")

    elif choice == "5":
        value = int(input("New CPU usage: "))
        if 0 <= value <= 100:
            cpu = value
            print("CPU updated.")
            logs.append("CPU usage changed")
        else:
            print("Incorrect value.")

    elif choice == "6":
        value = int(input("New RAM usage: "))
        if 0 <= value <= 100:
            ram = value
            print("RAM updated.")
            logs.append("RAM usage changed")
        else:
            print("Incorrect value.")

    elif choice == "7":
        value = int(input("New disk usage: "))
        if 0 <= value <= 100:
            disk = value
            print("Disk updated.")
            logs.append("Disk usage changed")
        else:
            print("Incorrect value.")

    elif choice == "8":
        print("\n--- LOGS ---")
        if len(logs) == 0:
            print("No logs found.")
        else:
            for log in logs:
                print("-", log)

    elif choice == "9":
        print("\n--- SYSTEM STATUS ---")
        print("CPU:", cpu, "%")
        print("RAM:", ram, "%")
        print("Disk:", disk, "%")
        if cpu >= 85 or ram >= 90 or disk >= 90:
            print("STATUS: CRITICAL")
        elif cpu >= 60 or ram >= 70 or disk >= 70:
            print("STATUS: WARNING")
        else:
            print("STATUS: NORMAL")

    elif choice == "10":
        print("\nStopping system...")
        time.sleep(1)
        print("System stopped.")
        break
    else:
        print("Unknown command.")