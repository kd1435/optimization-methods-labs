"""
Kokia turėtų būti stačiakampio gretasienio formos dėžė, kad vienetiniam paviršiausplotui jos tūris būtų maksimalus?

    Suprogramuokite gradientinio nusileidimo, greičiausiojo nusileidimo ir deformuojamo simplekso algoritmus.
    Laikant kintamaisiais dėžės priekinės ir galinės sienų plotų sumą, šoninių sienų plotų sumą, viršutinės ir apatinės sienų plotų sumą, aprašykite vienetinio dėžės paviršiaus ploto reikalavimą ir dėžės tūrio pakelto kvadratu funkciją.
    Iš vienetinio paviršiaus ploto reikalavimo išveskite vieno iš kintamojo išraišką per kitus.
    Aprašykite tikslo funkciją f(X) taip, kad optimizavimo uždavinys būtų formuluojamas be apribojimų: min f(X).
    Išveskite ir aprašykite tikslo funkcijos gradiento funkciją.
    Apskaičiuokite tikslo ir gradiento funkcijų reikšmes taškuose X0= (0,0), X1=(1,1) ir Xm= (1/2, 1/2)
    Minimizuokite suformuluotą uždavinį naudojant suprogramuotus optimizavimo algoritmus pradedant iš taškų X0, X1 ir Xm.
    Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius priklausomai nuo pradinio taško.
    Vizualizuokite tikslo funkciją ir bandymo taškus.
"""

import numpy as np
import sympy as sp
from dataclasses import dataclass

# TODO: Program gradient descent algorithm

@dataclass
class OptimizationResult:
    x_min: float
    xs: list[float]
    iterations: int
    function_calls: int

class ObjectiveFunction:
    def __init__(self, *xs) -> None:
        self.calls = 0

        # self.x: list[sp.Symbol] = [sp.symbols('x{i}')]
        # self.expr: sp.Expr = (self.x**2 - 5)**2 / 4 # type: ignore

        # self.expr_prime: sp.Expr = sp.diff(self.expr, self.x)
        # self.expr_double_prime: sp.Expr = sp.diff(self.expr, self.x, 2)

        # self.f = sp.lambdify(self.x, self.expr, 'numpy')
        # self.df = sp.lambdify(self.x, self.expr_prime, 'numpy')
        # self.ddf = sp.lambdify(self.x, self.expr_double_prime, 'numpy')

    # def __call__(self, *x: float) -> float:
    #     self.calls += 1
    #     return self.f(x)
    
    # def first_derivative(self, x:float) -> float:
    #     self.calls += 1
    #     return self.df(x)
    
    # def second_derivative(self, x:float) -> float:
    #     self.calls += 1
    #     return self.ddf(x)
    
    # def print_symbolic(self):
    #     print("f(x) =", self.expr)
    #     print("f'(x) =", self.expr_prime)
    #     print("f''(x) =", self.expr_double_prime)
    
    def reset(self):
        self.calls = 0

# TODO: Implement gradient calculation
# TODO: Implement partial derivative calculation
def gradient_descent(
        objective_function: ObjectiveFunction,
        step_size: float = 0.05,
        x_i: float = 5) -> OptimizationResult:
    
    x_min: float | None = None
    objective_function.reset()
    # f = objective_function.__call__
    
    print("GRADIENT DESCENT OPTIMIZATION METHOD")
    print("Before initiating the method")
    print("-------------------------------------------------")
    print()

    xs = []
    iteration: int = 0
    
    # Loop end
    return OptimizationResult(
        x_min=x_min, 
        xs=xs, 
        iterations=iteration, 
        function_calls=objective_function.calls,
    )

def main():
    print("Hello from lab2!")


if __name__ == "__main__":
    main()
