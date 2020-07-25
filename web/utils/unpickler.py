import pickle


class CustomUnpickler(pickle.Unpickler):
    """ Custom class that requires a binary file to read a pickle data stream."""
    def find_class(self, module, name):
        if module == "__main__":
            module = "app"
        return super().find_class(module, name)