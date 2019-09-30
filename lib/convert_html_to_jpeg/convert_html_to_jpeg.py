import imgkit

class convert_html_to_jpeg():

    def __init__(self, html_file):
        self.html_file = html_file

    def test(self):
        print(self.html_file)

    def convert(self, name=None):
        """Convert the html file into a .jpg file"""
        if not name:
            jpg_file_name = self.html_file.split('.')[0] + '.jpg'
            print(f'No name given. Using {jpg_file_name}')
        else:
            jpg_file_name = name
        imgkit.from_file(self.html_file, jpg_file_name)