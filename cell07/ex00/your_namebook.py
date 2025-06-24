def array_of_names(namelist):
    arr_names = []
    for key, val in namelist.items():
        arr_names.append(f"{key.capitalize()} {val.capitalize()}")
    return arr_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))