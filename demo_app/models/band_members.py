class BandMember:
    def __init__(self, name):
        self.name = name
        self.role = self.__class__.__name__.lower()
        self.noise = None

    def make_noise(self):
        return f'{self.name} the {self.role} goes {self.noise}'

    def to_dict(self):
        return {
            'member_name': self.name,
            'member_role': self.role
        }


class Guitarist(BandMember):
    def __init__(self, name):
        super().__init__(name)
        self.noise = 'djang djang'


class Bassist(BandMember):
    def __init__(self, name):
        super().__init__(name)
        self.noise = 'dum dum'


class Drummer(BandMember):
    def __init__(self, name):
        super().__init__(name)
        self.noise = 'boom boom'
