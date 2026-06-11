import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="trackr",
        description="Trackr Project Management Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add-user command
    add_user = subparsers.add_parser(
        "add-user",
        help="Add a new user"
    )

    add_user.add_argument(
        "--name",
        required=True
    )

    add_user.add_argument(
        "--email",
        required=True
    )

    # list-users command
    subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
    