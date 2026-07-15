import re

with open("data.txt", "r") as file:
    content = file.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, content)

with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Emails extracted successfully!")
print("Total Emails Found:", len(emails))