def get_all_file_names(text):
    lines = text.split('\n')
    reference = ''
    files = []

    for line in lines:
        file_name = line.split('#')[0]
        if reference != (file_name := line.split('#')[0]) and (len(file_name) > 1):
            files.append(file_name)
            reference = file_name

    return files
