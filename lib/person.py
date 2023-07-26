import ipdb


class Person:
    def __init__(self, name, bank_account=25, happiness=8, hygiene=8):
        self._name = name
        self.bank_account = bank_account
        self.happiness = happiness
        self.hygiene = hygiene

    def get_name(self):
        return self._name

    def is_clean(self):
        if self.hygiene > 7:
            return True
        else:
            return False

    def is_happy(self):
        if self.happiness > 7:
            return True
        else:
            return False

    def get_paid(self, amount):
        self.bank_account += amount
        print("all about the benjamins")

    def take_bath(self):
        self.hygiene += 4
        print("♪ Rub-a-dub just relaxing in the tub ♫")

    def work_out(self):
        self.happiness += 2
        self.hygiene -= 3
        print("♪ another one bites the dust ♫")

    def call_friend(self, friend):
        self.happiness += 3
        friend.happiness += 3
        print(f"Hi {friend.name}! It's {self.name}. How are you?")

    def start_conversation(self, friend, topic):
        if topic == "politics":
            self.happiness -= 2
            friend.happiness -= 2
            print("blah blah partisan blah lobbyist")
        elif topic == "weather":
            self.happiness += 1
            friend.happiness += 1
            print("blah blah sun blah rain")
        else:
            print("blah blah blah blah blah")

    name = property(get_name, None)


friend = Person("Ethan")
christina = Person("Christina")

ipdb.set_trace()
