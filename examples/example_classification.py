"""
A real-life-ish example for classifier parameter selection
"""

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from timeoutpool import TimeoutJobBase, TimeoutPool

N = 1000
N_DIM = 5

X = np.random.random_sample((N, N_DIM))
y = np.random.randint(2, size=(N))

rf_params = [
        {'max_depth': 3, 'n_estimators': 10, 'n_jobs': 1, 'random_state': 5},
        {'max_depth': 3, 'n_estimators': 100, 'n_jobs': 1, 'random_state': 5},
        {'max_depth': 3, 'n_estimators': 1000, 'n_jobs': 1, 'random_state': 5},
        {'max_depth': 5, 'n_estimators': 10, 'n_jobs': 1, 'random_state': 5},
        {'max_depth': 5, 'n_estimators': 100, 'n_jobs': 1, 'random_state': 5},
        {'max_depth': 5, 'n_estimators': 1000, 'n_jobs': 1, 'random_state': 5}]

class RFJob(TimeoutJobBase):
    """
    A job fitting and evaluating a random forest parameterization
    """
    def __init__(self, params):
        """
        The constructor of the job

        Args:
            params (dict): a random forest parameterization
        """
        self.params = params

    def execute(self):
        """
        Executes the job

        Returns:
            dict: the result of the evaluation
        """
        forest = RandomForestClassifier(**self.params)
        preds = forest.fit(X, y).predict_proba(X)
        return {'auc': roc_auc_score(y, preds[:, 1]),
                'timeout': False,
                'params': self.params}

    def timeout(self):
        """
        The method called when a job times out

        Returns:
            dict: the timeout result
        """
        return {'auc': -1,
                'timeout': True,
                'params': self.params}

tp = TimeoutPool(n_jobs=2, timeout=1)

results = tp.execute((RFJob(param) for param in rf_params))

pd.set_option('display.max_colwidth', 200)
print(pd.DataFrame(results))
