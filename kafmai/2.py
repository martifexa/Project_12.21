def remove_spaces(str_with_spaces: str)->str:
    return ' '.join(str.split(str_with_spaces))
a = "Hello     world"
print(a)
a = remove_spaces(a)
print(a)
