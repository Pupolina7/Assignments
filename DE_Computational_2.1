#include <iostream>
#include <vector>
#include <cmath>

double f_x(double x, double y) {
    return y;
}

double f_y(double x, double y) {
    return -4 * x;
}

void eulerMethod(int n, std::vector<double>& t_points, std::vector<double>& x_points, std::vector<double>& y_points) {
    double h = M_PI / (n - 1);
    double x = 1.0;
    double y = 2.0;
    for (int i = 0; i < n; ++i) {
        t_points.push_back(i * h);
        x_points.push_back(x);
        y_points.push_back(y);
        double x_new = x + h * f_x(x, y);
        double y_new = y + h * f_y(x, y);
        x = x_new;
        y = y_new;
    }
}

void improvedEulerMethod(int n, std::vector<double>& t_points, std::vector<double>& x_points, std::vector<double>& y_points) {
    double h = M_PI / (n - 1);
    double x = 1.0;
    double y = 2.0;

    for (int i = 0; i < n; ++i) {
        t_points.push_back(i * h);
        x_points.push_back(x);
        y_points.push_back(y);
        double k1_x = f_x(x, y);
        double k1_y = f_y(x, y);
        double k2_x = f_x(x + h * k1_x, y + h * k1_y);
        double k2_y = f_y(x + h * k1_x, y + h * k1_y);
        double x_new = x + h * 0.5 * (k1_x + k2_x);
        double y_new = y + h * 0.5 * (k1_y + k2_y);
        x = x_new;
        y = y_new;
    }
}

void rungeKuttaMethod(int n, std::vector<double>& t_points, std::vector<double>& x_points, std::vector<double>& y_points) {
    double h = M_PI / (n - 1);
    double x = 1.0;
    double y = 2.0;

    for (int i = 0; i < n; ++i) {
        t_points.push_back(i * h);
        x_points.push_back(x);
        y_points.push_back(y);
        double k1_x = h * f_x(x, y);
        double k1_y = h * f_y(x, y);
        double k2_x = h * f_x(x + 0.5 * h, y + 0.5 * k1_y);
        double k2_y = h * f_y(x + 0.5 * k1_x, y + 0.5 * k1_y);
        double k3_x = h * f_x(x + 0.5 * h, y + 0.5 * k2_y);
        double k3_y = h * f_y(x + 0.5 * k2_x, y + 0.5 * k2_y);
        double k4_x = h * f_x(x + h, y + k3_y);
        double k4_y = h * f_y(x + k3_x, y + k3_y);
        double x_new = x + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6;
        double y_new = y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6;
        x = x_new;
        y = y_new;
    }
}

int main() {
    int n, task;
    std::cin >> n;
    std::cin >> task;
    std::vector<double> t_points, x_points, y_points;
    std::cout << std::fixed;
    std::cout.precision(5);
    switch (task) {
        case 1:
            eulerMethod(n, t_points, x_points, y_points);
            std::cout << "ti=" << std::endl;
            break;
        case 2:
            improvedEulerMethod(n, t_points, x_points, y_points);
            std::cout << "ti=" << std::endl;
            break;
        case 3:
            rungeKuttaMethod(n, t_points, x_points, y_points);
            std::cout << "ti=" << std::endl;
            break;
        default:
            std::cout << "Invalid task number.\n";
            return 1;
    }
    for (double t : t_points) {
        std::cout << t << " ";
    }
    std::cout << std::endl;

    if (task == 1) {
        std::cout << "Euler_xi=" << std::endl;
    } else if (task == 2) {
        std::cout << "iEuler_xi=" << std::endl;
    } else {
        std::cout << "RK4_xi=" << std::endl;
    }
    for (double x : x_points) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    if (task == 1) {
        std::cout << "Euler_yi=" << std::endl;
    } else if (task == 2) {
        std::cout << "iEuler_yi=" << std::endl;
    } else {
        std::cout << "RK4_yi=" << std::endl;
    }
    for (double y : y_points) {
        std::cout << y << " ";
    }
    std::cout << std::endl;
    return 0;
}
