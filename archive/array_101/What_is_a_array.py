
class DVD :
    def __init__(self, name, release_year, director):
        self,name = name    
        self.release_year = release_year
        self.director = director

    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.release_year}"

dvd_collection = [None] * 15

dvd_collection[0] = DVD("Highest to lowest", 2015, "Denzel Washingtion")


print(dvd_collection)