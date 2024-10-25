class LibraryItem:
    def __init__(self, id, name, director, rating, count, image_path=None):
        self.id = id
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = count
        self.image_path = image_path


    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("ID must be a number")
        if value < 0:
            raise ValueError("Invalid id")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if not value:
            raise ValueError("Director cannot be empty")
        self._director = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value == "":
            raise ValueError("Rating cannot be empty!")
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Rating must be a number")
        if not (1 <= value <= 5) :
            raise ValueError("Rating must be a number between 1 and 5!")
        self._rating = value

    @property
    def play_count(self):
        return self._play_count

    @play_count.setter
    def play_count(self, value):
        if value == "":
            raise ValueError("Play count cannot be empty")
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Play count must be a number")
        if  value < 0 :
            raise ValueError("Play count must be a non-negative integer")
        self._play_count = value

    @property
    def image_path(self):
        return self._image_path
    
    @image_path.setter
    def image_path(self, image_path):
        if image_path == "":
            raise ValueError('Image path can not be empty')
        self._image_path = image_path

    def save_item(self):
        return f"{self.id},{self.name},{self.director},{self.stars()}"

    def info(self):
        return f"{self.name} - {self.director} - {self.stars()}"
    
    def name_info(self):
        return f"{self.name}"

    def stars(self):
        stars = ""
        for i in range(int(self.rating)):
            stars += "*"
        return stars
