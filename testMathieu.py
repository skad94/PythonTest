import copy as copy
from List import LinkedList
from PythonTest import *
from algo import Solution
import sys
sys.path.append(r'C:\Users\skamta\Desktop\TestGit\PythonTest\PythonTest')
#import nom_du_module
#nom_du_module.nom_de_la_methode()


def checkProba(array):
    res = 0
    for p_i in array:
        if p_i < 0:
            return False
        if p_i > 1:
            return False
        else:
            res = res + p_i
    if res == 1:
        return True
    else:
        return False
        
    

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
        if checkProba(probabilities):
            self.probabilities = probabilities
        else:
            print("please fill with true Proba")
    
    def setProba(self,state,proba):
        self.state = state
        if checkProba(proba):
            self.probabilities = proba
        else:
            print("please fill with true Proba")

    def show_info(self):
        print(self.name)
        res = []
        for i in range(len(self.state)):
            res.append([self.state[i],self.probabilities[i]])
            print(res[-1])

    def __copy__(self):
        return type(self)(self.name,self.state.copy(), self.probabilities.copy())


class ProbaContinuous(Proba):
    def __init__(self, name,density_function):
        super().__init__(name)
        self.density_function = density_function

    def show_info(self):
        print("Type :", self.name)
        print("Density function :", self.density_function)

    def __copy__(self):
        return type(self)(self.name,self.density_function)

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
    # # Création d'une distribution de probabilité discrète
    # proba_discrete = ProbaDiscrete("manual Discrete", [1, 2, 3], [0.2, 0.5, 0.3])
    # proba_discrete2 = proba_discrete.__copy__()
    # #proba_discrete.show_info()
    # B = Bernouilli(0.4)
    # #B.show_info()


    # # Création d'une distribution de probabilité continue
    # def density(x):
    # # Fonction de densité avec intégrale égale à 1 sur l'intervalle [0, 2]
    #     if x < 0:
    #         return 0
    #     if x > 2:
    #         return 0
    #     else:
    #         return 0.5 * x ** 2

    # proba_continuous = ProbaContinuous("manual Continue",density)
    # proba_continuous_copy = proba_continuous.__copy__()
    # proba_continuous.show_info()
    # proba_continuous_copy.show_info()
    # numz = [8,8,5,6,8,8,5]
    # print(numz)
    # target = 8
    # tmp = Solution()
    # res = tmp.removeElement(numz,target)
    # print(res)
    print("sk")
    # l = LinkedList(10)
    # l.append(94)
    # l.append(7)
    # l.print_list()

# [1,3,5,6]
# 5
# [1,3,5,6]
# 2
# [1,3,5,6]
# 7
# [1,3,5,6]
# 8
# [1,3,5,6]
# 0