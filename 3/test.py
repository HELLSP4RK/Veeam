import os
import string
import time
from random import choices

from psutil import virtual_memory

from base import TestCase


class FilesListCase(TestCase):
    seconds = int(time.time())
    path = os.path.expanduser('~')
    content = os.listdir(path)

    def prep(self):
        super(FilesListCase, self).prep()
        if self.seconds % 2 != 0:
            message = 'Seconds are not divisible by 2. Program run is aborted'
            self.logging(message)
            raise SystemExit(message)

    def run(self):
        super(FilesListCase, self).run()
        print('\n'.join(self.content))


class RandomFileCase(TestCase):
    required_memory_size = 1_073_741_824
    total_memory = virtual_memory().total
    file_size = 1_048_576
    content = ''.join(choices(string.ascii_letters + string.digits, k=file_size))

    def prep(self):
        super(RandomFileCase, self).prep()
        if self.total_memory < self.required_memory_size:
            message = 'RAM of your PC is less than 1Gb. Program run is aborted'
            self.logging(message)
            raise SystemExit(message)

    def run(self):
        super(RandomFileCase, self).run()
        self.logging('Creating file "test"...')
        with open("test", "w") as file:
            file.write(self.content)

    def clean_up(self):
        super(RandomFileCase, self).clean_up()
        try:
            os.remove('test')
            self.logging('File removed')
        except OSError:
            message = "File doesn't exist"
            self.logging(message)
            print(message)
