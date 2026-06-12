import argparse #import python built in argparse... understand how to create commands.
from utils.storage import save_json, load_json  # importing the two functions so i can use them.


def main(): #create a function called main..instead of putting code in the file we put it inside function.
    parser = argparse.ArgumentParser() #responsible for understanding and processing command line input.
    subparsers = parser.add_subparsers(dest="command") #recognise all commands

    # ---------------- USER ----------------
    add_user_cmd = subparsers.add_parser("add-user") # create command called add user.
    add_user_cmd.add_argument("--name", required=True) #   define what arguments required
    add_user_cmd.add_argument("--email", required=True)

    subparsers.add_parser("list-users")   # retrieve and display.

    

    # list-users command


    args = parser.parse_args() # reading what user has typed and store it.

    data = load_json("db.json") # loading existing data into the program.

    if "users" not in data:
        data = {
            "users": [],
        }

    # ---------------- ADD USER ----------------
    if args.command == "add-user":
        data["users"].append({
            "name": args.name,
            "email": args.email,
            "projects": []
        })
        save_json("db.json", data)
        print("User added")

    # ---------------- LIST USERS ----------------
    elif args.command == "list-users":
        print([u["name"] for u in data["users"]])

    # ---------------- ADD PROJECT ----------------
    elif args.command == "add-project":
        for u in data["users"]:
            if u["name"] == args.user:
                u["projects"].append({
                    "title": args.title,
                    "description": args.description,
                    "tasks": []
                })
                save_json("db.json", data)
                print("Project added")
                return
        print("User not found")

    # ---------------- LIST PROJECTS ----------------
    elif args.command == "list-projects":
        for u in data["users"]:
            if u["name"] == args.user:
                print([p["title"] for p in u["projects"]])
                return
        print([])

    # ---------------- ADD TASK ----------------
    elif args.command == "add-task":
        for u in data["users"]:   #loop through users
            for p in u["projects"]:
                if p["title"] == args.project:
                    p["tasks"].append({
                        "title": args.title,
                        "status": "pending"
                    })
                    save_json("db.json", data)
                    print("Task added")
                    return
        print("Project not found")

    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
    