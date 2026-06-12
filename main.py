import argparse
from utils.storage import save_json, load_json


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # user

    add_user_cmd = subparsers.add_parser("add-user")
    add_user_cmd.add_argument("--name", required=True)
    add_user_cmd.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    # project

    add_project_cmd = subparsers.add_parser("add-project")
    add_project_cmd.add_argument("--user", required=True)
    add_project_cmd.add_argument("--title", required=True)
    add_project_cmd.add_argument("--description", default="")

    list_projects_cmd = subparsers.add_parser("list-projects")
    list_projects_cmd.add_argument("--user", required=True)

    # tasks

    add_task_cmd = subparsers.add_parser("add-task")
    add_task_cmd.add_argument("--project", required=True)
    add_task_cmd.add_argument("--title", required=True)

    # parse-args

    args = parser.parse_args()

    # load data

    data = load_json("db.json")

    if not isinstance(data, dict):
        data = {"users": []}

    if "users" not in data:
        data["users"] = []

    # add user

    if args.command == "add-user":
        data["users"].append({
            "name": args.name,
            "email": args.email,
            "projects": []
        })
        save_json("db.json", data)
        print("User added")

    #  list users

    elif args.command == "list-users":
        print([u["name"] for u in data["users"]])

    # project

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

    # list project
    elif args.command == "list-projects":
        for u in data["users"]:
            if u["name"] == args.user:
                print([p["title"] for p in u["projects"]])
                return
        print([])

    # add task
    elif args.command == "add-task":
        for u in data["users"]:
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