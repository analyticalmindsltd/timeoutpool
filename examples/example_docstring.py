"""
The example as it appears in the docstring
"""

import time
from timeoutpool import TimeoutPool, TimeoutJobBase

class SleepJob(TimeoutJobBase):
    """
    A sleep job class for illustration
    """
    def __init__(self, sleep):
        """
        Constructor of the job

        Args:
            sleep (float): the time to sleep
        """
        TimeoutJobBase.__init__(self)
        self.sleep = sleep

    def execute(self):
        """
        The job to be executed.

        Returns:
            dict: the result of the job
        """
        begin = time.time()

        time.sleep(self.sleep)

        return {'sleep': self.sleep, 'slept': f'{time.time() - begin:.2f}'}

    def timeout(self):
        """
        The default result returned when the job times out.

        Returns:
            dict: the default result
        """
        return {'sleep': self.sleep, 'slept': None}

jobs = [SleepJob(sleep) for sleep in range(1, 5)]

tpool = TimeoutPool(n_jobs=2, timeout=2.5)

begin_execution = time.time()

results = tpool.execute(jobs)

print(results)

print(f'runtime {time.time() - begin_execution:.2f}')
