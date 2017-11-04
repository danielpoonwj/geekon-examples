import demo_app.models.band_members


class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member_name, member_role):
        # Command Dispatch pattern
        # http://zqpythonic.qiniucdn.com/data/20060526140550/index.html#command-dispatch-pattern
        klass = getattr(demo_app.models.band_members, member_role.capitalize())
        self.members.append(klass(member_name))

    def perform(self):
        return ', '.join(member.make_noise() for member in self.members)

    @staticmethod
    def __members_to_dict(members):
        return list(map(lambda x: x.to_dict(), members))

    def get_members_by_role(self, member_role):
        # Attribute error would thrown if invalid member role
        getattr(demo_app.models.band_members, member_role.capitalize())

        return self.__members_to_dict(
            [member for member in self.members if member.role == member_role]
        )

    def to_dict(self):
        return {
            'band_name': self.name,
            'members': self.__members_to_dict(self.members),
            'performance': self.perform()
        }
