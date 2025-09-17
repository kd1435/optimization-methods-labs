"""
1. Suprogramuokite vienmačio optimizavimo intervalo dalijimo pusiau, auksinio pjūvio ir Niutono metodo algoritmus.

2. Aprašykite tikslo funkciją f(x) = (x^2 − 5)^2 / 4

3. Minimizuokite šią funkciją intervalo dalijimo pusiau ir auksinio pjūvio metodais intervale [0,10] iki tikslumo 10^−4 bei Niutono metodu nuo x0 = 5 kol žingsnio ilgis didesnis už 10^−4.

4. Palyginkite rezultatus: gauti sprendiniai, rastas funkcijos minimumo įvertis, atliktų žingsnių ir funkcijų skaičiavimų skaičius.

5. Vizualizuokite tikslo funkciją ir bandymo taškus.

"""

def objective_function(x):
    return (x**2 - 5)**2 / 4

# print (objective_function(1))

def bisection_method():
    lipschitz_constant = 0.05

    interval = [0, 10]
    left_bound = interval[0]
    right_bound = interval[1]
    interval_length = right_bound - left_bound

    iteration = 0
    while (interval_length > lipschitz_constant):
        x_middle = (left_bound + right_bound) / 2
        x1 = left_bound + interval_length / 4
        x2 = right_bound - interval_length / 4

        f_x1 = objective_function(x1)
        f_x2 = objective_function(x2)
        f_x_middle = objective_function(x_middle)

        if (f_x1 < f_x_middle):
            right_bound = x_middle

        elif (f_x2 < f_x_middle):
            left_bound = x_middle

        else:
            left_bound = x1
            right_bound = x2

        print("Current iteration:", iteration)
        print("Interval:", [left_bound, right_bound])
        print("Interval length:", interval_length)
        print("x1:", x1)
        print("x2:", x2)
        print("x_middle:", x_middle)
        print("f_x1:", f_x1)
        print("f_x2:", f_x2)
        print("f_x_middle:", f_x_middle)
        print("-------------------------------------------------")
        print()

        interval_length = right_bound - left_bound
        iteration += 1

bisection_method()