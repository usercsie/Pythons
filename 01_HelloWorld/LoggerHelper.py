class Dumper:
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(Dumper):
    pass


t = Thing()
t.name = "Nyarlathontep"
t.feature = "ichor"
t.age = "eldrith"
t.dump()
