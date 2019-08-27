from pygns3.Struct import Struct
from pygns3.API import GNS3API


class GNS3Drawing:
    """An SVG object inside a project"""

    def __init__(self, drawing):
        self._drawing = drawing
        self.project_id = drawing['project_id']
        self.drawing_id = drawing['drawing_id']
        self.__dict__.update(Struct(**drawing).__dict__)

    def __repr__(self):
        return f'GNS3Drawing({self.project_id}, {self.drawing_id})'

    def __str__(self):
        max_key_width = max(map(len, self._drawing.keys()))
        setting_items = [f'    {k:{max_key_width + 1}} {v}' for k, v in self._drawing.items()]
        settings = '\n'.join(setting_items) + '\n'
        return 'GNS3Drawing:\n' + settings + ''

class GNS3Symbol:
    """A Symbol"""

    def __init__(self, symbol):
        self._symbol = symbol
        self.builtin = symbol['builtin']
        self.file_name = symbol['filename']
        self.symbol_id = symbol['symbol_id']

    def __repr__(self):
        return f'GNS3Symbol({self.symbol_id})'

    def __str__(self):
        attributes = ', '.join([f'{attr}: {val}' for attr, val in self.__dict__.items()])
        return f'GNS3Symbol({attributes})'
