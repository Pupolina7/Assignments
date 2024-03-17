#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

double exactSolution(double x) {
    return sin(x);
}

std::vector<double> eulerMethod(int n, double h) {
    std::vector<double> y(n);
    for (int i = 0; i < n - 1; ++i) {
        double x = i * h;
        y[i] = y[i - 1] + h * cos(x);
    }
    for (int i = n - 1; i >=0; --i) {
        y[i] = y [i - 1];
    }
    return y;
}

std::vector<double> improvedEulerMethod(int n, double h) {
    std::vector<double> y(n);
    for (int i = 0; i < n; ++i) {
        double x = i * h;
        double k1 = h * cos(x);
        double k2 = h * cos(x + h);
        y[i] = y[i - 1] + 0.5 * (k1 + k2);
    }
    for (int i = n - 1; i >=0; --i) {
        y[i] = y [i - 1];
    }
    return y;
}

std::vector<double> rungeKuttaMethod(int n, double h) {
    std::vector<double> y(n);
    for (int i = 0; i < n; ++i) {
        double x = i * h;
        double k1 = h * cos(x);
        double k2 = h * cos(x + 0.5 * h);
        double k3 = h * cos(x + 0.5 * h);
        double k4 = h * cos(x + h);
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0;
    }
    for (int i = n - 1; i >=0; --i) {
        y[i] = y [i - 1];
    }
    return y;
}

std::vector<double> calculateLocalErrors(const std::vector<double>& numericalSolution, int n, double h) {
    std::vector<double> localErrors(n);
    for (int i = 0; i < n; ++i) {
        double x = i * h;
        localErrors[i] = std::fabs(exactSolution(x) - numericalSolution[i]);
    }
    return localErrors;
}

double calculateGlobalError(const std::vector<double>& localErrors) {
    return *std::max_element(localErrors.begin(), localErrors.end());
}


int main() {
    int n, n1, n2, task;
    std::cin >> n >> n1 >> n2 >> task;
    std::cout << std::fixed;
    std::cout.precision(5);
    double h = M_PI / (n - 1);

    switch (task) {
        case 1:
            std::cout << "xi=" << std::endl;
            for (double i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\ny(xi)=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << exactSolution(i * h) << " ";
            break;
        case 2:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\nEuler_yi=" << std::endl;
            for (double val : eulerMethod(n, h))
                std::cout << val << " ";
            break;
        case 3:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\niEuler_yi=" << std::endl;
            for (double val : improvedEulerMethod(n, h))
                std::cout << val << " ";
            break;
        case 4:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\nRK4_yi=" << std::endl;
            for (double val : rungeKuttaMethod(n, h))
                std::cout << val << " ";
            break;
        case 5:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\nEuler_LE(xi)=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << fabs(exactSolution(i * h) - eulerMethod(n, h)[i]) << " ";
            break;
        case 6:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\niEuler_LE(xi)=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << fabs(exactSolution(i * h) - improvedEulerMethod(n, h)[i]) << " ";
            break;
        case 7:
            std::cout << "xi=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << i * h << " ";
            std::cout << "\nRK4_LE(xi)=" << std::endl;
            for (int i = 0; i < n; ++i)
                std::cout << fabs(exactSolution(i * h) - rungeKuttaMethod(n, h)[i]) << " ";
            break;
        case 8:
            std::cout << "ni=" << std::endl;
            for (int i = n1; i <= n2; ++i)
                std::cout << i << " ";
            std::cout << "\nEuler_GE(n)=" << std::endl;
            for (int i = n1; i <= n2; ++i) {
                double hi = M_PI / (i - 1);
                std::vector<double> numericalSolution = eulerMethod(i, hi);
                std::vector<double> localErrors = calculateLocalErrors(numericalSolution, i, hi);
                double globalError = calculateGlobalError(localErrors);
                std::cout << globalError << " ";
            }
            break;
        case 9:
            std::cout << "ni=" << std::endl;
            for (int i = n1; i <= n2; ++i)
                std::cout << i << " ";
            std::cout << "\niEuler_GE(n)=" << std::endl;
            for (int i = n1; i <= n2; ++i) {
                double hi = M_PI / (i - 1);
                std::vector<double> numericalSolution = improvedEulerMethod(i, hi);
                std::vector<double> localErrors = calculateLocalErrors(numericalSolution, i, hi);
                double globalError = calculateGlobalError(localErrors);
                std::cout << globalError << " ";
            }
            break;

        case 10:
            std::cout << "ni=" << std::endl;
            for (int i = n1; i <= n2; ++i)
                std::cout << i << " ";
            std::cout << "\nRK4_GE(n)=" << std::endl;
            for (int i = n1; i <= n2; ++i) {
                double hi = M_PI / (i - 1);
                std::vector<double> numericalSolution = rungeKuttaMethod(i, hi);
                std::vector<double> localErrors = calculateLocalErrors(numericalSolution, i, hi);
                double globalError = calculateGlobalError(localErrors);
                std::cout << globalError << " ";
            }
            break;
        default:
            std::cout << "Invalid task number." << std::endl;
            break;
    }

    return 0;
}
