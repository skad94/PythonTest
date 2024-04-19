import copy as copy
class Proba:
    def __init__(self, name):
        self.name = name

    def __copy__(self):
        return type(self)(self.name)
    
    def show_name(self):
        print("Name :", self.name)


class ProbaDiscrete(Proba):
    def __init__(self, name, state, probabilities):
        super().__init__(name)
        self.state = state
        self.probabilities = probabilities

    def show_info(self):
        print(self.name)
        res = []
        for i in range(len(self.state)):
            res.append([self.state[i],self.probabilities[i]])
            print(res[-1])

    def __copy__(self):
        res = type(self)(self.name,self.state.copy(), self.probabilities.copy())
        return res


class ProbaContinuous(Proba):
    def __init__(self, name,density_function):
        super().__init__(name)
        self.density_function = density_function

    def show_info(self):
        print("Type :", self.name)
        print("Density function :", self.density_function)

    def __copy__(self):
        res = type(self)(self.name,self.density_function)
        return res

class Bernouilli(ProbaDiscrete):
     def __init__(self, param):
        if param <0:
            raise Exception(f"Bernoulli param must be above 0 ({param})")
        if param >1:
            raise Exception(f"Bernoulli param must be below 1 ({param})")
        self.name = self.__class__.__name__
        self.param = param
        self.state = [0,1]
        self.probabilities = [param,1-param]

     def __copy__(self):
        return type(self)(self.values.copy(), self.probabilities.copy())
    
# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une distribution de probabilité discrète
    proba_discrete = ProbaDiscrete("manual Discrete", [1, 2, 3], [0.2, 0.5, 0.3])
    proba_discrete2 = proba_discrete.__copy__()
    #proba_discrete.show_info()
    B = Bernouilli(0.4)
    #B.show_info()


    # Création d'une distribution de probabilité continue
    def density(x):
    # Fonction de densité avec intégrale égale à 1 sur l'intervalle [0, 2]
        if x < 0:
            return 0
        if x > 2:
            return 0
        else:
            return 0.5 * x ** 2

    proba_continuous = ProbaContinuous("manual Continue",density)
    proba_continuous_copy = proba_continuous.__copy__()
    proba_continuous.show_info()
    proba_continuous_copy.show_info()
