# File Access Permission Simulation

role = input("Enter Role: ").lower()

print("Permissions:")

if role == "admin":
    print("Read")
    print("Write")
    print("Delete")
elif role == "faculty":
    print("Read")
    print("Write")
elif role == "student":
    print("Read Only")
else:
    print("Invalid Role")
