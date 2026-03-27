#!/usr/bin/python3

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error")
        return
    if not isinstance(attendees, list):
        print("Error")
        return
    if template == "":
        print("Template is empty, no output files generated")
        return
    if attendees == []:
        print("No data provided, no output files generated")
        return

    for index, x in enumerate (attendees, start=1):
        for i in x:
            if x[i] is None:
                x[i] = "N/A"
        texte = template.format(**x)
        with open (f"output_{index}.txt", "w") as f:
            f.write (texte)