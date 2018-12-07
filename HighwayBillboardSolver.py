from billboard_problem.RevenueCalculator import RevenueCalculator


def main():
    m = 100
    x = [6, 7, 12, 13, 14]
    revenue = [5, 6, 5, 3, 1]
    t = 5
    revenue_calculator = RevenueCalculator()
    print(revenue_calculator.max_revenue_tabulation(m,x,revenue,t))
    print(revenue_calculator.max_revenue_memoization(x, revenue, t))
    print(revenue_calculator.dictionary)

if __name__ == '__main__':
    main()
