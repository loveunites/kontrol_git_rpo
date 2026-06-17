import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def show_project_title():
    print("Git practice project started")


def show_student_info():
    student_name = "ФАМИЛИЯ ИМЯ"
    group = "НАЗВАНИЕ ГРУППЫ"
    print(f"Student: {student_name}")
    print(f"Group: {group}")


def show_git_topics():
    topics = [
        "README.md",
        ".gitignore",
        "commits",
        "branches",
        "merge",
        "fetch",
        "pull",
        "conflicts",
    ]

    print("Practice topics:")
    for topic in topics:
        print(f"- {topic}")


def main():
    show_project_title()
    show_student_info()
    show_git_topics()


if __name__ == "__main__":
    main()
