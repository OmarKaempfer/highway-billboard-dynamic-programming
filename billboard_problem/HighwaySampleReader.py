class HighwaySampleReader:

    @staticmethod
    def read_all_samples(file_path):
        file = open(file_path, "r")
        samples = []

        if file.mode == 'r':
            lines = file.readlines()

        for i in range(0, len(lines), 2):
            samples.append([int(j) for j in lines[i].strip().split(",")])
            samples.append([int(j) for j in lines[i+1].strip().split(",")])

        return samples
