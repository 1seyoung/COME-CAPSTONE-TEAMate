from rx import create


class EnvironmentManagement:
    def __init__(self):
        self.environment = {}

    def set_environment_data(self, name, data):
        self.environment[name] = data

    def del_environment_data(self, name):
        del self.environment[name]

    def get_source(self):
        print(self.environment)
        return create(self.object_rx)

    def object_rx(self, observer, scheduler):
        observer.on_next(self.environment)
        observer.on_completed()
