from prefect import task, flow

@task()
def task_example():
    return "Hello World"

@flow(name="{{cookiecutter.flow_name}}")
def main_flow():
    """
    Here you write your main flow code and call your tasks and/or subflows.
    """
    pass
