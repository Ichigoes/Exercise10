username = input()

command_data = input().split()

while command_data[0] != "Registration":

    if command_data == "Registration":
        break

    if command_data[0] == "Letters":
        if command_data[1] == "Lower":
            username = username.lower()
            print(username)
        elif command_data[1] == "Upper":
            username = username.upper()
            print(username)

    elif command_data[0] == "Reverse":
        start = int(command_data[1])
        end = int(command_data[2])
        if start and end > 0 and start and end < len(username):
            part = username[end:start - 1:-1]
            print(part)

    elif command_data[0] == "Substring":
        substring = command_data[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif command_data[0] == "Replace":
        char = command_data[1]
        if char in username:
            username = username.replace(char, "-")
            print(username)

    elif command_data[0] == "IsValid":
        char = command_data[1]
        if char in username:
            print("Valid")
        else:
            print(f"{char} must be contained in your username.")

    command_data = input().split()