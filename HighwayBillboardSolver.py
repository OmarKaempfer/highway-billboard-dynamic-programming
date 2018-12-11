from billboard_problem.HighwaySampleReader import HighwaySampleReader
from billboard_problem.RevenueCalculator import RevenueCalculator
from billboard_problem.HighwaySampleGenerator import HighwaySampleGenerator


def main():
    samples = HighwaySampleReader.read_all_samples("asdasd.txt")
    HighwaySampleGenerator.generate_new_extended_highway_to_file("asdasd.txt", samples[0], samples[1], 3, 2, 10)
    samples = HighwaySampleReader.read_all_samples("asdasd.txt")
    for element in samples:
        print(element)


if __name__ == '__main__':
    main()
