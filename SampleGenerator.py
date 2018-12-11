import argparse

from billboard_problem.HighwaySampleGenerator import HighwaySampleGenerator
from billboard_problem.HighwaySampleReader import HighwaySampleReader


def main():
    parse_args()
    exit(0)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="The path of the file where the new samples will be appended")
    parser.add_argument("starting_point", type=int, help="The minimum starting position to be generated")
    parser.add_argument("upper_distance_bound", type=int, help="The maximum distance between two positions")
    parser.add_argument("upper_revenue_bound", type=int, help="The maximum revenue one billboard can provide")
    parser.add_argument("size", type=int, help="The number of billboards to be placed")
    parser.add_argument("-e", "--extend", help="We want to extend an existing sample. The path to the file "
                                               "containing the sample to be extended must be provided. Only "
                                               "the top two samples of the file will be used.")
    args = parser.parse_args()
    if args.extend is None:
        HighwaySampleGenerator.generate_new_sample_to_file(args.starting_point, args.file_path,
                                                           args.upper_distance_bound, args.upper_revenue_bound,
                                                           args.size)
        print("New sample generated successfully")
    else:
        samples = HighwaySampleReader.read_all_samples(args.extend)

        HighwaySampleGenerator.generate_new_extended_highway_to_file(args.file_path, samples[0], samples[1],
                                                                     args.upper_distance_bound,
                                                                     args.upper_revenue_bound, args.size)
        print("Sample extended successfully")


if __name__ == '__main__':
    main()
