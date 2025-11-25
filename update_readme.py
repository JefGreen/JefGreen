import datetime

def update_readme_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z") # Customize date format as needed
    readme_path = "README.md"

    with open(readme_path, "r") as f:
        content = f.read()

    new_content = content.replace(
        "<!-- DYNAMIC_DATE -->",
        f"<!-- DYNAMIC_DATE --> {current_date} (UTC)" # Add timezone if relevant
    )

    with open(readme_path, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme_date()