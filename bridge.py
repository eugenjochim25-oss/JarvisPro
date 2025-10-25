import os
print("💻 System Bridge läuft...")
while True:
    cmd = input("Befehl eingeben: ")
    if cmd.lower() in ["exit", "quit"]:
        break
    os.system(cmd)
