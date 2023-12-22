class IterativeModel:
    def __init__(self, iterations):
        self.iterations = iterations

    def iterate(self):
        for i in range(self.iterations):
            print("\nIteration {}".format(i + 1))
            self.define_requirements()
            self.design_model()
            self.implement_model()
            self.test_model()

    def define_requirements(self):
        print("Define model requirements")

    def design_model(self):
        print("Design the model")

    def implement_model(self):
        print("Implement the model")

    def test_model(self):
        print("Test the model")


iterations = 5

model_iterative = IterativeModel(iterations)
model_iterative.iterate()
