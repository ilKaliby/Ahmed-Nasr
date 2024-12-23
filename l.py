class Bird:
    def fly(self):
        return "I can fly"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly")


def let_bird_fly(bird: Bird):
    try:
        print(bird.fly())
    except NotImplementedError as e:
        print(e)

sparrow = Sparrow()
penguin = Penguin()

let_bird_fly(sparrow)
let_bird_fly(penguin)