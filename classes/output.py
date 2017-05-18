import os, csv, pickle

class Output:
    u"""
    出力層のクラスです。
    """
    def __init__(self):
        # CSVを格納しているディレクトリのパス
        self.csv_dirpath = os.getcwd() + '/csv'

    def write_in_csv(self, my_hand, tile, dora):
        u"""
        結果をCSVに書き込みます。
        """
        csv_filepath = self.csv_dirpath + '/results.csv'
        csvlist = []
        for hand in my_hand:
            csvlist.append(hand)
        csvlist.append(dora)
        csvlist.append(tile)

        with open(csv_filepath, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(csvlist)

        return

    def write_in_pickle(self, weight_parameter, bias_parameter):
        u"""
        結果をpickelに書き込みます。
        """
        pickle_filepath = os.getcwd() + '/pickle/output_results.pickle'
        results = {}
        results['W'] = weight_parameter
        results['b'] = bias_parameter

        with open(pickle_filepath, 'wb') as f:
            writer = pickle.dump(results, f)

