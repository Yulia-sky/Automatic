class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def say_track(self):
        print(self.track)

    def say_to_address(self):
        print(self.to_address)

    def say_from_address(self):
        print(self.from_address)

    def say_cost(self):
        print(self.cost)

    def say_track(self):
        print(self.track)