"""
An example of querying PIDs with the TimeoutJob interface and generators
"""

import os

from timeoutpool import TimeoutJobBase, TimeoutPool

class PIDJob(TimeoutJobBase):
    """
    The job class querying the PID of the executor process
    """
    def __init__(self):
        """
        The constructor of the object
        """
        TimeoutJobBase.__init__(self)

    def execute(self):
        """
        Execute the job

        Returns:
            int: the PID of the executor process
        """
        return os.getpid()

    def timeout(self):
        """
        The function called in case of timeout

        Returns:
            int: the default return value
        """
        return -1

tpool = TimeoutPool(n_jobs=2, timeout=1)

results = tpool.execute((PIDJob() for _ in range(10)))

print(results)
