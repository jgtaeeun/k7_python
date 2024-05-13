def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')       #함수return값이 str이므로 musician은 str이다.
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)