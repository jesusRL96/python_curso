import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        # print(name)
        self.current = name
        if self.current == 'CD':
            print("--------CD-------")
            print("ID: {}".format(attrs['id']))

    def characters(self, content):
        if self.current == "TITLE":
            # print(content)
            self.title = content
        elif self.current == "ARTIST":
            # print(content)
            self.artist = content
        elif self.current == "COUNTRY":
            # print(content)
            self.country = content
        elif self.current == "COMPANY":
            # print(content)
            self.company = content
        elif self.current == "PRICE":
            # print(content)
            self.price = content
        elif self.current == "YEAR":
            # print(content)
            self.year = content
    
    def endElement(self, name):
        if self.current == "TITLE":
            print(f"Title: {self.title}")
        elif self.current == "COUNTRY":
            print(f"Country: {self.country}")
        elif self.current == "ARTIST":
            print(f"Artist: {self.artist}")
        self.current = ''

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('cd_catalog.xml')