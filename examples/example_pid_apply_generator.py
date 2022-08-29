"""
An example querying PIDs with the .apply interface and a generator of jobs
"""

import os

from timeoutpool import TimeoutPool

def worker(*_args):
    """
    The actual job querying the PID of the process.

    Args:
        _args (list): the unsued positional arguments

    Returns:
        int: the PID of the executor process
    """
    return os.getpid()

tpool = TimeoutPool(n_jobs=2, timeout=1)

results = tpool.apply(worker, range(0, 10))

print(results)
