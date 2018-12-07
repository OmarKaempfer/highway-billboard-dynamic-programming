from billboard_problem.RevenueCalculator import *


def main():
    m = 20
    x = [6, 7, 12, 13, 14]
    revenue = [5, 6, 5, 3, 1]
    t = 5
    print(max_revenue_tabulation(m, x, revenue, t))


if __name__ == '__main__':
    main()
