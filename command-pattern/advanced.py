from abc import ABC, abstractmethod


# Command Interface
class Task(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


# ConcreteTask Classes
class AddTask(Task):
    def __init__(self, data, item):
        self.data = data
        self.item = item
        self.index = None

    def execute(self):
        self.data.append(self.item)
        self.index = len(self.data) - 1

    def unexecute(self):
        if self.index is not None:
            self.data.pop(self.index)


class RemoveTask(Task):
    def __init__(self, data, item):
        self.data = data
        self.item = item
        self.index = None

    def execute(self):
        self.index = self.data.index(self.item)
        self.data.pop(self.index)

    def unexecute(self):
        if self.index is not None:
            self.data.insert(self.index, self.item)


# Invoker Class
class TaskQueue:
    def __init__(self):
        self.history = []
        self.undo_history = []

    def execute_task(self, task):
        task.execute()
        self.history.append(task)
        self.undo_history.clear()

    def undo(self):
        if not self.history:
            return
        last_task = self.history.pop()
        last_task.unexecute()
        self.undo_history.append(last_task)

    def redo(self):
        if not self.undo_history:
            return
        last_undone = self.undo_history.pop()
        last_undone.execute()
        self.history.append(last_undone)


# Client Code
if __name__ == "__main__":
    data = [1, 2, 3, 1]
    add_task = AddTask(data, 4)
    remove_task = RemoveTask(data, 1)

    queue = TaskQueue()

    print("Initial data:", data)

    queue.execute_task(add_task)
    print("After adding 4:", data)

    queue.execute_task(remove_task)
    print("After removing 1:", data)

    queue.undo()
    print("After undo:", data)

    queue.undo()
    print("After second undo:", data)

    queue.redo()
    print("After redo:", data)

"""
> python command-pattern/advanced.py
Initial data: [1, 2, 3, 1]
After adding 4: [1, 2, 3, 1, 4]
After removing 1: [2, 3, 1, 4]
After undo: [1, 2, 3, 1, 4]
After second undo: [1, 2, 3, 1]
After redo: [1, 2, 3, 1, 4]
"""
