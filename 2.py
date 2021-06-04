import os
import sys
from hashlib import md5, sha1, sha256

BUF_SIZE = 262144


def main():
    input_file, files_directory = get_paths()
    with open(input_file, 'r') as opened_file:
        for line in opened_file.readlines():
            file_name, hash_type, checksum_hash = get_params_from_line(line)
            hash_type = hash_type.upper()
            sum_hash = get_sum_hash(hash_type)
            print(file_name, end=' ')
            try:
                with open(f'{files_directory}\\{file_name}', 'rb') as file:
                    while True:
                        data = file.read(BUF_SIZE)
                        if not data:
                            break
                        sum_hash.update(data)
                if checksum_hash == sum_hash.hexdigest():
                    print('OK')
                else:
                    print('FAIL')
            except FileNotFoundError:
                print('NOT FOUND')


def get_paths():
    try:
        input_file, files_directory = sys.argv[1:]
    except ValueError:
        raise SystemExit(f'You can run the program with the command "python {sys.argv[0]} <path to the input file> '
                         f'<path to the directory containing the files to check>"')
    return normalize_paths(input_file, files_directory)


def normalize_paths(*paths):
    normalized_paths = list()
    for path in paths:
        normalized_paths.append(os.path.abspath(path))
    return normalized_paths


def get_params_from_line(line):
    try:
        file_name, hash_type, checksum_hash = line.split()
    except ValueError:
        raise SystemExit(f'ERROR: {line}')
    return file_name, hash_type, checksum_hash


def get_sum_hash(hash_type):
    sum_hash = {
        'MD5': md5(),
        'SHA1': sha1(),
        'SHA256': sha256(),
    }
    try:
        return sum_hash[hash_type]
    except KeyError:
        raise SystemExit(f'Hash type {hash_type} is wrong')


if __name__ == '__main__':
    main()
