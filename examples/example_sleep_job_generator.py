"""
An example of a sleep job with the TimeoutJob interface and generators
"""

import time

from timeoutpool import TimeoutPool, TimeoutJobBase

sleeps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tpool = TimeoutPool(n_jobs=4, timeout=4)

class SleepJob(TimeoutJobBase):
    """
    The sleep job class
    """
    def __init__(self, sleep):
        """
        Constructor of the sleep job

        Args:
            sleep (float): the time to sleep
        """
        self.sleep = sleep

    def execute(self):
        """
        Execute the job

        Returns:
            dict: the summary of the job
        """
        time.sleep(self.sleep)
        return {'slept': self.sleep}

    def timeout(self):
        """
        The function called in case of timeout

        Returns:
            dict: the result in case of timeout
        """
        return {'slept': None}

results = tpool.execute((SleepJob(sleep) for sleep in sleeps))

print(results)
