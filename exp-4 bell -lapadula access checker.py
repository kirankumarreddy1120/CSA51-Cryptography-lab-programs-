# Bell-LaPadula Access Checker

levels = {
    "public": 1,
    "confidential": 2,
    "secret": 3,
    "top secret": 4
}

user_level = input("User Level: ").lower()
file_level = input("File Level: ").lower()
operation = input("Operation (Read/Write): ").lower()

u = levels[user_level]
f = levels[file_level]

if operation == "read":
    if u >= f:
        print("Access Allowed")
    else:
        print("Access Denied")
        print("Reason: No Read Up")

elif operation == "write":
    if u <= f:
        print("Access Allowed")
    else:
        print("Access Denied")
        print("Reason: No Write Down")

else:
    print("Invalid Operation")
