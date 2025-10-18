from math import sqrt
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from dataclasses import dataclass, field

"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

2. Aprašykite tikslo funkciją f(x) = (x^2 − 5)^2 / 4

3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^−4 bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.

4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.

5. Vizualizuokite tikslo funkciją ir bandymo taškus.
"""

@dataclass
class OptimizationResult:
    x_min: float
    xs: list[float]
    iterations: int
    function_calls: int
    tangents: list[tuple[float,float]] = field(default_factory=list)  

class ObjectiveFunction:
    def __init__(self) -> None:
        self.calls = 0

        self.x: sp.Symbol = sp.symbols('x')
        self.expr: sp.Expr = (self.x**2 - 5)**2 / 4 # type: ignore

        self.expr_prime: sp.Expr = sp.diff(self.expr, self.x)
        self.expr_double_prime: sp.Expr = sp.diff(self.expr, self.x, 2)

        self.f = sp.lambdify(self.x, self.expr, 'numpy')
        self.df = sp.lambdify(self.x, self.expr_prime, 'numpy')
        self.ddf = sp.lambdify(self.x, self.expr_double_prime, 'numpy')

    def __call__(self, x: float) -> float:
        self.calls += 1
        return self.f(x)
    
    def first_derivative(self, x:float) -> float:
        self.calls += 1
        return self.df(x)
    
    def second_derivative(self, x:float) -> float:
        self.calls += 1
        return self.ddf(x)
    
    def print_symbolic(self):
        print("f(x) =", self.expr)
        print("f'(x) =", self.expr_prime)
        print("f''(x) =", self.expr_double_prime)
    
    def reset(self):
        self.calls = 0

def print_variables(**kwargs):
    for name, value in kwargs.items():
        print(f"{name}: {value}")
    print("-------------------------------------------------")
    print()

def bisection_method(
        objective_function: ObjectiveFunction, 
        interval: tuple[int, int] = (0, 10), 
        tolerance_lipschitz_constant: float = 10**-4) -> OptimizationResult:
    
    # Points kept for plotting later
    x_min: float
    xs: list[float] = []
    
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length: float = right_bound - left_bound
    
    print("BISECTION OPTIMIZATION METHOD")
    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")
    print()

    objective_function.reset()
    f = objective_function.__call__

    x_middle: float = (left_bound + right_bound) / 2 # 1.
    x1: float | None = None
    x2: float | None = None
    f_x_middle: float = f(x_middle) # 1.
    f_x1: float | None = None
    f_x2: float | None = None

    iteration: int = 0
    while interval_length > tolerance_lipschitz_constant:
        interval_length = right_bound - left_bound
        
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print()
            
        x1 = left_bound + interval_length / 4 # 2.
        f_x1 = f(x1) # 2.

        xs.append(x1)
        xs.append(x_middle)
        
        if f_x1 < f_x_middle: # 3. x_middle becomes x_1
            right_bound = x_middle # 3.1
            x_middle = x1 # 3.2
            f_x_middle = f_x1 # 3.2
            print_variables(
                objective_function_calls=objective_function.calls,
                x1=x1,
                x_middle=x_middle,
                x2=x2,
                f_x1=f_x1,
                f_x_middle=f_x_middle,
                f_x2=f_x2
            )
            interval_length = right_bound - left_bound
            iteration += 1
            continue # 6. is while loop condition

        else: # 2.
            x2 = right_bound - interval_length / 4 # 2.
            f_x2 = f(x2) # 2.
            xs.append(x2)
        if f_x2 < f_x_middle: # 4. x_middle becomes x_2
            left_bound = x_middle # 4.1 
            x_middle = x2 # 4.2 
            f_x_middle = x2 # 4.2
        else: # 5. x_middle stays x_middle
            x_middle = x_middle
            left_bound = x1 # 5.1 
            right_bound = x2 # 5.1
            
        print_variables(
            objective_function_calls=objective_function.calls,
            x1=x1,
            x_middle=x_middle,
            x2=x2,
            f_x1=f_x1,
            f_x_middle=f_x_middle,
            f_x2=f_x2
        )
        interval_length = right_bound - left_bound
        iteration += 1
    # Loop end
    x_min: float = (left_bound + right_bound) / 2
    return OptimizationResult(
        x_min=x_min, 
        xs=xs, 
        iterations=iteration, 
        function_calls=objective_function.calls
    )
    
def golden_section_method(
        objective_function: ObjectiveFunction, 
        interval: tuple[int, int] = (0, 10), 
        tolerance_lipschitz_constant: float = 10**-4
        ) -> OptimizationResult:
    
    
    
    objective_function.reset()
    f = objective_function.__call__
    left_bound: float 
    right_bound: float 
    left_bound, right_bound = interval
    interval_length: float = right_bound - left_bound # 1.
    
    tau: float = (-1 + sqrt(5)) / 2
    x1: float = right_bound - tau * interval_length # 1.
    x2: float = left_bound + tau * interval_length # 1.
    f_x1: float = f(x1) # 1.
    f_x2: float = f(x2) # 1.

    # Points kept for plotting later
    xs: list[float] = [x1, x2]

    print("GOLDEN SECTION OPTIMIZATION METHOD")
    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("x1:", x1)
    print("x2:", x2)
    print("f_x1:", f_x1)
    print("f_x2:", f_x2)
    print("-------------------------------------------------")
    print()

    iteration: int = 0
    
    while interval_length > tolerance_lipschitz_constant:
        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print()
        
        if f_x2 < f_x1: # 2.
            left_bound = x1 # 2.1 remove interval [left_bound; x1)
            interval_length = right_bound - left_bound # 2.1 / 3.1
            x1 = x2 # 2.2
            f_x1 = f_x2
            x2 = left_bound + tau * interval_length # 2.3
            f_x2 = f(x2) # 2.3
            xs.append(x2)
        else: # 3.
            right_bound = x2 # 3.1 remove interval (x2; right_bound]
            interval_length = right_bound - left_bound # 2.1 / 3.1
            x2 = x1 # 3.2
            f_x2 = f_x1
            x1 = right_bound - tau * interval_length # 3.3
            f_x1 = f(x1) # 3.3
            xs.append(x1)

        print("objective_function_calls:", objective_function.calls)
        print_variables(
            left_bound=left_bound,
            right_bound=right_bound,
            interval_length=interval_length,
            x1=x1,
            x2=x2,
            f_x1=f_x1,
            f_x2=f_x2
        )
        iteration += 1

    x_min: float = (left_bound + right_bound) / 2
    return OptimizationResult(
        x_min=x_min, 
        xs=xs, 
        iterations=iteration, 
        function_calls=objective_function.calls
    )

# Minimizuokite Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.
def newton_method(objective_function: ObjectiveFunction, 
                  interval: tuple[int, int] = (0, 10), 
                  tolerance_lipschitz_constant: float = 10**-4, 
                  x_i: float = 5) -> OptimizationResult:
    objective_function.reset()
    f = objective_function.__call__
    df = objective_function.first_derivative
    ddf = objective_function.second_derivative
    left_bound: float = interval[0]
    right_bound: float = interval[1]
    interval_length: float = right_bound - left_bound
    
    print("NEWTON OPTIMIZATION METHOD")
    print("Before initiating the method")
    print("Interval:", [left_bound, right_bound])
    print("Interval length:", interval_length)
    print("-------------------------------------------------")
    print()

    xs = []
    tangents = []
    iteration: int = 0
    step_size: float = interval_length

    x_iplus1: float | None = None
    
    while step_size > tolerance_lipschitz_constant:
        print("Current iteration:", iteration)
        print()

        slope = df(x_i)
        tangents.append((x_i, slope))
        xs.append(x_i)

        # Newton update
        x_iplus1 = x_i - slope / ddf(x_i)
        step_size = abs(x_i - x_iplus1)
        
        x_i = x_iplus1
        
        print_variables(
            x_i=x_i,
            x_iplus1=x_iplus1,
            step_size=step_size,
            objective_function_calls=objective_function.calls
        )

        x_i = x_iplus1 
        
        iteration += 1
    # Loop end
    return OptimizationResult(
        x_min=x_i, 
        xs=xs, 
        iterations=iteration, 
        function_calls=objective_function.calls,
        tangents=tangents
    )

# TODO: Plot after finishing optimization algorithm with each method
f1 = ObjectiveFunction()
# Objective function curve
x_vals = np.linspace(0, 10, 400)
y_vals = f1.f(x_vals)

# Run optimization methods
res_bis = bisection_method(f1)
res_gold = golden_section_method(f1)
res_newton = newton_method(f1)

# Plot each method separately
plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(res_bis.xs, [f1.f(x) for x in res_bis.xs], s=30, color="red", label="Bisection")
plt.title("Bisection Method")
plt.legend()
plt.xlabel(f"Iterations: {res_bis.iterations} | Function calls: {res_bis.function_calls}")

plt.subplot(3,1,2)
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(res_gold.xs, [f1.f(x) for x in res_gold.xs], s=30, color="green", label="Golden Section")
plt.title("Golden Section Method")
plt.legend()
plt.xlabel(f"Iterations: {res_gold.iterations} | Function calls: {res_gold.function_calls}")

plt.subplot(3,1,3)
for x0, slope in res_newton.tangents:
    y0 = f1.f(x0)
    tangent_line = slope * (x_vals - x0) + y0
    plt.plot(x_vals, tangent_line, '--', alpha=0.7)
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(res_newton.xs, [f1.f(x) for x in res_newton.xs], color="purple", label="Newton")
plt.title("Newton's Method")
plt.legend()
plt.xlabel(f"Iterations: {res_newton.iterations} | Function calls: {res_newton.function_calls}")

plt.tight_layout()
plt.show()