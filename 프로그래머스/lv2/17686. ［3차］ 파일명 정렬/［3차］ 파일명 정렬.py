def extract(file):
    head, number, tail = '', '', ''
    for char in file:
        if not number and not char.isdigit():
            head += char
        elif not tail and char.isdigit():
            number += char
        else:
            tail += char
    return [head.upper(), int(number), tail]

def solution(files):
    sorted_files = sorted(files, key = lambda x: (extract(x)[0], extract(x)[1], files.index(x)))
    return sorted_files
