Getting Started
***************

What is `timeoutpool`?
========================

The package implements a distributed processing pool with the possibility to time-out each job independently.

The use-case to be solved by the package: there is an algorithm to be executed (potentially on various datasets) with various parameterizations. The goal is to discover the operation/limitations of the algorithm under various circumstances. Some parameterizations or some special datasets might lead to extremely long runtimes. The user is interested in the outcome of those cases when the algorithm finishes in N seconds.

In order to utilize all available resources (usually more than one CPU cores), some multiprocessing solution is needed, which continouosly monitors the execution time of the jobs, and if the runtime of a job exceeds the timeout limit, shuts it down and starts the next job immediately.

For various reasons, we found that this functionality is not available out-of-the-box in the popular distributed computing toolkits of Python, like `multiprocessing`, `joblib`, `concurrent.futures`. Although these packages have some timeout functionalities, they are not applied at the job/process level, but for an entire set or pool of jobs, timing out the entire batch even if one job times out.

The `timeoutpool` package implements the aforementioned functionality in terms of threads from the `threading` package and processes from `multiprocessing` package. The user can specify a list of jobs to be executed (through an iterator or generator), the number of worker processes (N) and the timeout limit (T). The `TimeoutPool` object then starts N threads pooling the jobs to N worker processes, each monitored by watchdog threads. If the runtime of a job exceeds T, the process is killed and `None` is returned or some predefined method is executed.
