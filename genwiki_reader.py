class GenWikiReader:
    data_name2folder = {
        'full': 'genwiki/train/full/',
        'fine': 'genwiki/train/fine/',
        'test': 'genwiki/test/'
    }
    sample_file = data_name2folder['fine'] + 'part_1.json'
    url_data = 'https://drive.google.com/uc?id=19IRK07e7RTKGUqTyNTEigECWAMIMgFav&export=download'

    def __init__(self):
        pass

    def read(self, data_name='all'):
        import os
        import json
        from glob import glob

        if not os.path.isfile(self.sample_file):
            self.download()

        if data_name in {'fine', 'full'}:
            data_names = [data_name]
        else:
            data_names = self.data_name2folder.keys()

        all_data = {}
        for name in data_names:
            folder = self.data_name2folder[name]
            tmpl = folder + (
                'part_' if name in {'fine', 'full'} else '') + '*.json'
            files = glob(tmpl)

            data = []
            for file in files:
                with open(file) as f:
                    datum = json.load(f)
                    data.extend(datum)
            all_data[name] = data
            print('[Info] There are {} samples in the GenWiki-{} dataset'
                  .format(len(all_data[name]), name))

        if data_name in {'fine', 'full'}:
            return all_data[data_name]
        else:
            return all_data

    def print_sample(self):
        import json
        import random

        with open(self.sample_file) as f:
            data = json.load(f)

        random.shuffle(data)
        print('[Info] The 1st random example:')
        print(json.dumps(data[0], indent=4))
        print('-----------')
        print('[Info] The 2nd random example:')
        print(json.dumps(data[1], indent=4))

    def download(self):
        import os

        if not os.path.isfile(self.sample_file):
            if not os.path.isfile('genwiki.zip'):
                from torchtext.utils import download_from_url
                print('[Info] No existing data detected. Start downloading...')
                download_from_url(self.url_data, root='.')
            os.system('unzip genwiki.zip')


if __name__ == '__main__':
    gw = GenWikiReader()
    gw.download()
    gw.read()
    fine_data = gw.read(data_name='fine')
    gw.print_sample()
