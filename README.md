# test_mlflow
### env python3.8
### terminal:
`pip3 install mlflow==1.26.0`

`python3 test.py`

### output:

```
Traceback (most recent call last):
  File "train.py", line 40, in <module>
    train()
  File "train.py", line 19, in train
    error = 1 / 0
ZeroDivisionError: division by zero
Active run: None
end_time 1653661423338
run_id: d302841f538347f78968c0ca3dc37370; status: FINISHED
2022/05/27 22:23:43 ERROR mlflow.cli: === Run (ID 'd302841f538347f78968c0ca3dc37370') failed ===
```
