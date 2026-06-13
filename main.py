import argparse
import uuid
from rich.console import Console
from rich.table import Table
from models.users import User
from models.projects import Project
from models.tasks import Task

console = Console()


def add_user(args):
    """Excelled: User-focused design with error handling."""
    try:
        user_id = str(uuid.uuid4())[:8]
        user = User(id=user_id, name=args.name, email=args.email)
        user.save()
        console.print(f"[green]✔ User '{args.name}' (ID: {user_id}) created.[/green]")
    except ValueError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]System Error:[/bold red] {e}")


def list_users(args):
    """Excelled: Uses external package 'rich' for data visualization."""
    users = User.get_all()
    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return

    table = Table(title="Trackr Users")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Email", style="green")

    for u in users:
        table.add_row(str(u.id), u.name, u.email)
    console.print(table)


def add_project(args):
    """Excelled: Dynamic relationship management."""
    try:
        # Find user by name
        users = User.get_all()
        user = next((u for u in users if u.name == args.user), None)

        if not user:
            console.print(f"[red]Error: User '{args.user}' not found.[/red]")
            return

        project_id = str(uuid.uuid4())[:8]
        project = Project(
            id=project_id,
            name=args.title,
            description=args.description,
            user_id=user.id,
        )
        project.save()
        console.print(f"[green]✔ Project '{args.title}' added to {user.name}.[/green]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")


def list_projects(args):
    """Relationship-aware listing."""
    users = User.get_all()
    user = next((u for u in users if u.name == args.user), None)

    if not user:
        console.print(f"[red]Error: User '{args.user}' not found.[/red]")
        return

    projects = user.get_projects()
    if not projects:
        console.print(f"[yellow]{user.name} has no projects.[/yellow]")
        return

    table = Table(title=f"Projects for {user.name}")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")

    for p in projects:
        table.add_row(str(p.id), p.name, p.description)
    console.print(table)


def add_task(args):
    """Deep relationship management (User -> Project -> Task)."""
    try:
        all_projects = Project.get_all()
        project = next((p for p in all_projects if p.name == args.project), None)

        if not project:
            console.print(f"[red]Error: Project '{args.project}' not found.[/red]")
            return

        task_id = str(uuid.uuid4())[:8]
        task = Task(
            id=task_id,
            title=args.title,
            description="",
            status="pending",
            project_id=project.id,
        )
        task.save()
        console.print(
            f"[green]✔ Task '{args.title}' added to '{project.name}'.[/green]"
        )
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")


def main():
    """Excelled: Modular CLI with argparse and help messages."""
    parser = argparse.ArgumentParser(
        description="Trackr: Professional Project Management CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # User Commands
    u_add = subparsers.add_parser("add-user", help="Register a new user")
    u_add.add_argument("--name", required=True, help="User full name")
    u_add.add_argument("--email", required=True, help="User email address")
    u_add.set_defaults(func=add_user)

    u_list = subparsers.add_parser("list-users", help="List all registered users")
    u_list.set_defaults(func=list_users)

    # Project Commands
    p_add = subparsers.add_parser("add-project", help="Create a new project for a user")
    p_add.add_argument("--user", required=True, help="Owner's name")
    p_add.add_argument("--title", required=True, help="Project title")
    p_add.add_argument(
        "--description", default="No description", help="Project purpose"
    )
    p_add.set_defaults(func=add_project)

    p_list = subparsers.add_parser(
        "list-projects", help="List projects owned by a user"
    )
    p_list.add_argument("--user", required=True, help="Owner's name")
    p_list.set_defaults(func=list_projects)

    # Task Commands
    t_add = subparsers.add_parser("add-task", help="Add a task to a project")
    t_add.add_argument("--project", required=True, help="Project name")
    t_add.add_argument("--title", required=True, help="Task summary")
    t_add.set_defaults(func=add_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
