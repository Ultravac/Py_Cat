class cat:

    def __init__(self, age, color, sound):
        self.age = age
        self.color = color
        self.sound = sound

    def  cat_sounds (self):
        if self.sound == "miau":
            print("Happy Cat")
        elif self.sound == "ssss":
            print("Angry Cat")
        else:
            print("Not sound")
        

cat_new = cat(50,"RED","miau")

cat_sentiment = cat_new.cat_sounds()

print(cat_sentiment)

