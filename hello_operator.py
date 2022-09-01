# from airflow.models.baseoperator import BaseOperator


# class HelloOperator(BaseOperator): #custom operator class
#     def __init__(self, name: str, **kwargs) -> None:
#         super().__init__(**kwargs)
#         self.name = name

#     def execute(self, context):
#         message = f"Hello {self.name}"   #print msg
#         print(message)
#         return message


class HelloOperator():
    def __init__() -> None:
        super().__init__()

    def execute():
        message = "Hello Smit"
        print(message)
        return message

