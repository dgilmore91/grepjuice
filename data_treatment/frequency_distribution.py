class FrequencyDistribution:

    def __init__(self, data):
        # Add count of data when instatiating - data should be
        # list/set or other iterable
        try:
            self.data = data
            self.data_count = len(data)
            self.distribution = self.generate_counts(normalised=True)
        except TypeError:
            print("Expected data as list")

    def generate_counts(self, normalised=False):
        # Generates a list of dictionaries that have the key:value
        # of item:count for given data. Returns normalised distribution if
        # normalised = True
        counts_list = []
        data_set = set(self.data)

        for item in data_set:
            count_for_item = self.data.count(item)
            if normalised:
                count_for_item = float(count_for_item) / self.data_count
            print ("COUNT:", count_for_item)
            count_dictionary = {str(item): count_for_item}
            counts_list.append(count_dictionary)

        return counts_list
