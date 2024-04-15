# l = ['S',94,"toto"]
# print(type(l))
# print("t = ", l)
# print("now set")
# s={'lepain',94,'toto',94}
# print(type(s))
# print("s = ", s)

def testDoc(a,b):
    """ 
    Here where the doc should be
    Beware of the 0 it's not supposed to be here
    """
    return 2*a+b*9*a-4/b
#print(testDoc.__doc__)
fruits = ['apples', 'oranges', 'bananas']
quantities = [5,3,4]
prices = [1.5,2.25,0.89]
res = []
for x in range(0,3):
    res.append([fruits[x],quantities[x],prices[x]])
#print(res)
res.append([False,False,False])
#print(any(res))
##################################################
#################DECORATOR########################
##################################################
# def decoTest(fun):
#     print("je joue " + fun.__name__)
#     fun()
#     print("je finis " + fun.__name__)


#decoTest(func("je","suis Mafia K1 fry"))

def print_decorator(function):
    print("je suis dans " + print_decorator.__name__)
    print("je finis la deco")
    def new_function(*args, **kwargs):
        print('Appel de la fonction {} avec args={} et kwargs={}'.format(
            function.__name__, args, kwargs))
        ret = function(*args, **kwargs)
        print('Retour: {}'.format(ret))
        return ret
    print("back dans la deco ")
    return new_function

def add(x,y):
    return x+y
add = print_decorator(add)
add(91,3)
