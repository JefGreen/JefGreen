import datetime

def update_readme_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z") # Customize date format as needed
    readme_path = "README.md"

    with open(readme_path, "r") as f:
        content = f.read()


    # TODO: use a regex to match the url what ever the date is and replace it with the current date and time
    # new_content = content.replace(
    #     <img src=f"https://tryhackme-images.s3.amazonaws.com/streak/Some1ShouldPatchThis.png#{current_date}" alt="Streak">
    # )

    # with open(readme_path, "w") as f:
    #     f.write(new_content)

if __name__ == "__main__":
    update_readme_date()