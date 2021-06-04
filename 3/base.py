import datetime


class TestCase:

    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        self.logging(f'Preparing "{self.tc_id} {self.name}"...')

    def run(self):
        self.logging(f'Running "{self.tc_id} {self.name}"...')

    def clean_up(self):
        self.logging(f'Cleaning up "{self.tc_id} {self.name}"...')

    def execute(self):
        self.prep()
        self.run()
        self.clean_up()
        self.logging('Complete!')

    def logging(self, message):
        time_point = datetime.datetime.now()
        with open('log.log', 'a') as log:
            log.write(f'{time_point}: {message}\n')
