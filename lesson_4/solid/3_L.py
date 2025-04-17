""" L - Liskov Substitution """


class Bird:

    def voice(self) -> str:
        return "tweet"

class FlyingBird(Bird):
    def fly(self):
        print("I am flying")



class Eagle(FlyingBird):
    def voice(self) -> str:
        return "aaaaar"


class Pinguin(Bird):
    def fly(self):
        raise NotImplementedError

    def voice(self) -> list:
        return ["tweet", "aar"]



def send_bird_to_fly(bird: FlyingBird):
    print(f"Send {bird.__class__.__name__} Fly!")
    bird.fly()


def bird_loud_voice(bird: Bird):
    x = bird.voice()
    print(x)



# send_bird_to_fly(Pinguin())
bird_loud_voice(Pinguin())
