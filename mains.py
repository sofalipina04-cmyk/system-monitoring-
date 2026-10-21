def check_cpu(cpu):
    print("CPU usage:", cpu, "%")

    if cpu < 60:
        print("Status: NORMAL")
    elif cpu < 85:
        print("Status: HIGH")
    else:
        print("Status: CRITICAL")

check_cpu(35)