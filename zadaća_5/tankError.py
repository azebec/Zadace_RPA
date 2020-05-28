class tankError(Exception):
    def __init__(self,code):
        self.error_message = ''
        self.error_dict = {
            000:'ERROR-000: Nespecificirana pogreška',
            101:'ERROR-101: Unijeta vrijednost nije ispravna. Unesite ponuđeno.'
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        print("Opis greške: {}".format(self.error_message))
