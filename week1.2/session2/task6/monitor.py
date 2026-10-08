# Week 1.2, Session 2: Task 6

machine_temp = int(input("machine temperature: "))
machine_pressure = int(input("machine pressure: "))
machine_operating = int(input("machine in operation(0/1): "))

high_temp = False
high_pressure = False

log_file = open("machine_log.txt", "w")

if 80 < machine_temp:
    high_temp = True
    print("machine too hot, shutdown")
elif 50 < machine_temp < 80:
    print("machine within thermal operating limits")
elif machine_temp < 50:
    print("machine temperature low")

if 100 < machine_pressure:
    high_pressure = True
    print("machine pressure high. recommend maintenance")
elif 70 < machine_pressure < 100:
    print("machine pressure stable")
elif machine_pressure < 70:
    print("machine pressure low")

log_file.write(f"current temperature={machine_temp}")
log_file.write(f"current pressure={machine_pressure}")

if machine_operating == 1:
    if high_temp or high_pressure:
        print("machine operating in unsafe conditions. recommend shut down")
        log_file.write("shutting down machine due to unsage conditions")
    else:
        print("machine opperating normaly")
        log_file.write("no actions taken")
else:
    print("machine not opperating. no action needed")
