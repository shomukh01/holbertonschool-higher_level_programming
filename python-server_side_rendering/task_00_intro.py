def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"

            content = content.replace(
                "{" + placeholder + "}", str(value)
            )

        with open(f"output_{index}.txt", "w") as file:
            file.write(content)
