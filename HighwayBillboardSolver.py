import argparse
import pickle
import time

from billboard_problem.HighwaySampleReader import HighwaySampleReader
from billboard_problem.RevenueCalculator import RevenueCalculator


def main():
    parse_args()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path of the file with the samples to be resolved")
    parser.add_argument("minimum_distance", type=int, help="The minimum distance between two billboards. A billboard "
                                                           "can be placed if no billboard is placed within "
                                                           "minimum_distance miles")
    parser.add_argument("-t", "--tabulation", action="store_true",
                        help="Solve with tabulation. Prints the time it takes.")
    parser.add_argument("-m", "--memoization", action="store_true",
                        help="Solve with memoization. Prints the time it takes.")

    args = parser.parse_args()
    samples = HighwaySampleReader.read_all_samples(args.file_path)

    if args.tabulation is True:
        solve_all_tabulation(samples, args.minimum_distance)

    if args.memoization is True:
        solve_all_memoization(samples, args.minimum_distance)


def solve_all_tabulation(samples, minimum_distance):
    for i in range(0, len(samples), 2):
        print("[TAB] Solving:")
        start_time = time.time()
        print("\nresult: ", RevenueCalculator.max_revenue_tabulation(samples[i], samples[i + 1], minimum_distance))
        elapsed_time = time.time() - start_time
        print("time: ", elapsed_time, " s", "\n")


def solve_all_memoization(samples, minimum_distance):
    revenue_calculator = RevenueCalculator()

    try:
        dict_file = open('dict.dat', 'rb')
        revenue_calculator.set_dictionary(pickle.load(dict_file))
    except:
        pass

    for i in range(0, len(samples), 2):
        print("[MEM] Solving:")
        start_time = time.time()
        print("\nresult: ", revenue_calculator.max_revenue_memoization(samples[i], samples[i + 1], minimum_distance))
        elapsed_time = time.time() - start_time
        print("time: ", elapsed_time, " s", "\n")

    try:
        dict_file = open('dict.dat', 'wb')
        pickle.dump(revenue_calculator.dictionary, dict_file)
    except:
        pass


if __name__ == '__main__':
    main()
