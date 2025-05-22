import re


def person_validator(person):
    errors = []
    if not (type(person[0]) == int and person[0]>0):
        errors.append('Person ID must be an integer > 0')

    if not (type(person[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[1])):
        errors.append('Person Name is Invalid')


    if not (type(person[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[2])):
        errors.append('Person Family is Invalid')

    if not (type(person[3]) == int and person[3]>0):
        errors.append('Person Account Amount must be an integer > 0')

    return errors


