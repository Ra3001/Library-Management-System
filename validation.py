def get_positive_integer(message):
    while True:
        value = input(message)
        if value.isdigit():
            number = int(value)
            if number > 0:
                return number
        print("Please enter a positive integer.")


def get_non_empty_text(message):
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("Input cannot be empty.")


def find_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None
