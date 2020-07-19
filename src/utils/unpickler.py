import pickle


class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            module = "app"
        return super().find_class(module, name)