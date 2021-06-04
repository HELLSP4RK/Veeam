import os
from shutil import copy
from xml.etree.ElementTree import parse


def main():
    files = xml_to_list()
    for file in files:
        full_filepath, destination_path = get_paths(file)
        if not check_paths(full_filepath, destination_path):
            continue
        copy(full_filepath, destination_path)


def xml_to_list():
    tree = parse('files.xml')
    root = tree.getroot()
    files = list()
    for file in root:
        if file.tag == 'file':
            files.append(file.attrib)
        else:
            xml_error()
    return files


def get_paths(file):
    try:
        full_filepath, destination_path = normalize_paths(f"{file['source_path']}\\{file['file_name']}",
                                                          file['destination_path'])
        return full_filepath, destination_path
    except KeyError:
        xml_error()


def normalize_paths(*paths):
    normalized_paths = list()
    for path in paths:
        normalized_paths.append(os.path.abspath(path))
    return normalized_paths


def check_paths(*paths):
    for path in paths:
        if not os.path.exists(path):
            print(f"{path} doesn't exist")
            return False
    return True


def xml_error():
    raise SystemExit('''XML-file structure is wrong. Sample:
    <config>
        <file
                source_path="..."
                destination_path="..."
                file_name="..."
        />
        ...
    </config>''')


if __name__ == '__main__':
    main()
