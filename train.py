import atexit
import time
from random import random, randint

import mlflow


def train():
    mlflow.log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    mlflow.log_metric("foo", random())
    mlflow.log_metric("foo", random() + 1)
    mlflow.log_metric("foo", random() + 2)

    time.sleep(3)

    # error
    error = 1 / 0
    print(error)


def end_up():

    run_id = mlflow.active_run().info.run_id

    mlflow.end_run()
    # Check for any active runs
    print("Active run: {}".format(mlflow.active_run()))

    run = mlflow.get_run(run_id)
    print("end_time", run.info.end_time)
    # status is FINISHED
    print("run_id: {}; status: {}".format(run.info.run_id, run.info.status))


atexit.register(end_up)

if __name__ == "__main__":
    train()
