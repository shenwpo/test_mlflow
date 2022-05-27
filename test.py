import os

import mlflow

mlflow.run(
    os.getcwd(),
    entry_point="main",
    synchronous=False,
    parameters={},
    use_conda=False
)
