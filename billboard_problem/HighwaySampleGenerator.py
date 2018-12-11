import random


class HighwaySampleGenerator:

    @staticmethod
    def generate_random_highway(starting_point, upper_distance_bound, upper_revenue_bound, size):
        previous_distance = 0
        billboard_positions = []
        revenue_positions = []

        for i in range(0, size):
            previous_distance = random.randint(previous_distance + 1, previous_distance + upper_distance_bound)
            billboard_positions.append(previous_distance)
            revenue_positions.append(random.randint(0, upper_revenue_bound))

        return [billboard_positions, revenue_positions]

    @staticmethod
    def write_list_to_file(list_to_write, file_path):
        text_file = open(file_path, "a+")

        for element in list_to_write[:len(list_to_write) - 1]:
            print(element, ",", file=text_file, end='', sep='')

        print(list_to_write[len(list_to_write) - 1], file=text_file)

        text_file.close()

    @staticmethod
    def generate_new_sample_to_file(file_path, upper_distance_bound, upper_revenue_bound, size):
        sample = HighwaySampleGenerator.generate_random_highway(0, upper_distance_bound, upper_revenue_bound, size)
        HighwaySampleGenerator.write_list_to_file(sample[0], file_path)
        HighwaySampleGenerator.write_list_to_file(sample[1], file_path)

    @staticmethod
    def generate_new_extended_highway(positions, revenue, upper_distance_bound, upper_revenue_bound, size_of_extension):
        last_position = positions[len(positions) - 1]
        highway_extension = HighwaySampleGenerator.generate_random_highway(last_position, upper_distance_bound,
                                                                           upper_revenue_bound, size_of_extension)
        positions += highway_extension[0]
        revenue += highway_extension[1]

        return [positions, revenue]

    @staticmethod
    def generate_new_extended_highway_to_file(file_path, positions, revenue, upper_distance_bound, upper_revenue_bound,
                                              size_of_extension):
        sample = HighwaySampleGenerator.generate_new_extended_highway(positions, revenue, upper_distance_bound,
                                                                      upper_revenue_bound, size_of_extension)
        HighwaySampleGenerator.write_list_to_file(sample[0], file_path)
        HighwaySampleGenerator.write_list_to_file(sample[1], file_path)
