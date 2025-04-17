"""
I - interface segregation
"""

class GenericWorker:
    def work(self):
        ...

    def rest(self):
        ...


class Robot(GenericWorker):
    def work(self):
        print("Beep beep")

    def rest(self):
        raise NotImplementedError



class WorkerMixin:
    def work(self):
        print("Work!")


class RestableMixin:
    def rest(self):
        print("Tired. Rest!")




class HumanWorker(WorkerMixin, RestableMixin):
    ...


class RobotWorker(WorkerMixin):
    ...

class Boss(RestableMixin):
    ...

h = HumanWorker()

"""
Mixin
"""