import re

def solution(new_id):
    new_id = new_id.lower()

    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id)

    new_id = re.sub('\.\.+', '.', new_id)

    new_id = new_id.strip(".")

    if new_id == "":
        new_id = "a"

    if len(new_id) > 15:
        new_id = "".join(list(new_id)[:15])

    new_id = new_id.rstrip(".")

    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))