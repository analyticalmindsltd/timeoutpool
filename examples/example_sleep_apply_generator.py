"""
An example of a sleep job with the .apply interface and generators
"""

import time

from timeoutpool import TimeoutPool

sleeps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tpool = TimeoutPool(n_jobs=4, timeout=4)

def job(sleep):
    """
    The actual job

    Args:
        sleep (float): the time to sleep

    Returns:
        dict: the summary of the job
    """
    time.sleep(sleep)
    return {'slept': sleep}

results = tpool.apply(job, (sleep for sleep in sleeps))

print(results)
