import os, csv

class Output:
    u"""
    出力層のクラスです。
    """
    def __init__(self):
        # CSVを格納しているディレクトリのパス
        self.csv_dirpath = os.getcwd() + '/csv'

    def write_in_csv(self, my_hand, tile):
        u"""
        結果をpickelに書き込みます。
        """
        csv_filepath = self.csv_dirpath + '/results.csv'
        csvlist = []
        for hand in my_hand:
            csvlist.append(hand)
        csvlist.append(tile)
        print(csvlist)

        with open(csv_filepath, 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(csvlist)

        return


