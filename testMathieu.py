import copy as copy
class Proba:
    def __init__(self, name):
        self.name = name

    def __copy__(self):
        return type(self)(self.name)
    
    def show_name(self):
        print("Name :", self.name)


class ProbaDiscrete(Proba):
    def __init__(self, values, probabilities):
        self.state = values
        self.probabilities = probabilities

    def show_info(self):
        print("Values :", self.state)
        print("Probabilities :", self.probabilities)

    def __copy__(self):
        return type(self)(self.state.copy(), self.probabilities.copy())


class ProbaContinuous(Proba):
    def __init__(self, density_function):
        self.density_function = density_function

    def show_info(self):
        print("Type :", self.name)
        print("Density function :", self.density_function)

    def __copy__(self):
        return type(self)(self.density_function)

class Bernouilli(ProbaDiscrete):
     def __init__(self, param):
        if param <0:
            raise Exception(f"Bernoulli param must be above 0" ({param})")
        if param >1:
            raise Exception(f"Bernoulli param must be below 1" ({param})")
        self.param = param
        self.state = [0,1]
        self.probabilities = [param;1-param]

    def show_info(self):
        print("Parameter :", self.param)
        print("Values :", self.values)
        print("Probabilities :", self.probabilities)

    def __copy__(self):
        return type(self)(self.values.copy(), self.probabilities.copy())
    
# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une distribution de probabilité discrète
    proba_discrete = ProbaDiscrete([1, 2, 3], [0.2, 0.5, 0.3])
    proba_discrete_copy = copy.copy(proba_discrete)
    proba_discrete.show_info()
    proba_discrete_copy.show_info()

    # Création d'une distribution de probabilité continue
    def density(x):
    # Fonction de densité avec intégrale égale à 1 sur l'intervalle [0, 2]
        if x < 0:
            return 0
        if x > 2:
            return 0
        else:
            return 0.5 * x ** 2

    proba_continuous = ProbaContinuous(density)
    proba_continuous_copy = copy.copy(proba_continuous)
    proba_continuous.show_info()
    proba_continuous_copy.show_info()
