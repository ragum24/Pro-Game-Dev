class Animal:
    def __init__(self,name,phylum,Class,size,power,colour):
        self.name=name
        self.phylum=phylum
        self.Class=Class
        self.size=size
        self.power=power
        self.colour=colour
    def details(self):
        print(f"Name of the animal is {self.name}")
        print(f"Phylum of the animal is {self.phylum}")
        print(f"Class of the animal is {self.Class}")
        print(f"Size of the animal is {self.size}")
        print(f"Power of the animal is {self.power}")
        print(f"Colour of the animal is {self.colour}")
A1=Animal("Pig goose","Chordates","Aves","75-100 cm","Powerful enough to steal your lunch (what my teacher said)","mostly pale grey with a slight brown tint")
A1.details()
A1.size="75cm to 100cm"
A1.details() 
