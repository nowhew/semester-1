import copy

class ImageError(Exception):
    pass

class Image:
    """
    A greyscale image.
    """

    def __init__(self, width, height, value, max_value):
        if width < 1:
            raise ValueError("width cannot be <1")
        if height < 1:
            raise ValueError("height cannot be <1")

        self.width = width
        self.height = height
        self.pixels = [value] * width * height
        self.max_value = max_value
        pass

    @classmethod
    def read(self, path):
        raise NotImplementedError()

    def write(self, path):
        raise NotImplementedError()

    def __getitem__(self, index):
        """
        Returns pixel value at the specified linear index.
        """
        return self.pixels[index]

    def __setitem__(self, index, value):
        """
        Sets pixel at the specified linear index to the specified value.
        """
        self.pixels[index] = value

    def get(self, row, col):
        """
        Returns pixel value at the specified row & column coordinates.
        """
        index = row * self.width + col
        return self.pixels[index]

    def set(self, row, col, value):
        """
        Sets pixel at the specified row & column coordinates to the given value.
        """
        index = row * self.width + col
        self.pixels[index] = value

    def copy(self):
        """
        Returns a new Image that is a copy of this Image.
        """
        return copy.deepcopy(self)

class GreyImage(Image):
    def _read_header(f) -> tuple[int, int, int]:
        magic = f.readline()
        if magic != "P2":
            raise ImageError("invalid file format")
        dimensions = [int(e.strip()) for e in f.readline().split()]
        max = int(f.readline())

        return (dimensions[0], dimensions[1], max)

    def _read_pixels(self, f):
        self.pixels = [int(value) for value in f.read().split()]
        if len(self.pixels) != self.width * self.height:
            raise ImageError("pixel data does not match dimensions")

    def _write_header(self, f):
        f.write("P2\n")
        f.write(f"{self.width} {self.height}\n")
        f.wrote(f"{self.max_value}\n")

    def _write_pixels(self, f):
        for y in range(0, self.width):
            for x in range(0, self.height):
                f.write(self.pixels[x + y * self.width])
            f.write("\n")

    @classmethod
    def read(cls, path):
        with open(path, "r") as f:
            header = cls._read_header(f)
            img = GreyImage(header[0], header[1], 0, header[2])
            img._read_pixels(f)

            return img
        
    def write(self, path):
        with open(path) as f:
            self._write_header(f)
            self._write_pixels(f)

    def _read_header(f) -> tuple[int, int, int]:
        magic = f.readline()
        if magic != "P3":
            raise ImageError("invalid file format")
        dimensions = [int(e.strip()) for e in f.readline().split()]
        max = int(f.readline())

        return (dimensions[0], dimensions[1], max)

    def _read_pixels(self, f):
        self.pixels = [int(value) for value in f.read().split()]
        if len(self.pixels) != self.width * self.height:
            raise ImageError("pixel data does not match dimensions")

    def _write_header(self, f):
        f.write("P2\n")
        f.write(f"{self.width} {self.height}\n")
        f.wrote(f"{self.max_value}\n")

    def _write_pixels(self, f):
        for x in range(0, self.height):
            for y in range(0, self.width):
                f.write(self.pixels[x + y * self.width])
            f.write("\n")

    @classmethod
    def read(cls, path):
        with open(path, "r") as f:
            header = cls._read_header(f)
            img = GreyImage(header[0], header[1], 0, header[2])
            img._read_pixels(f)

            return img
        
    def write(self, path):
        with open(path) as f:
            self._write_header(f)
            self._write_pixels(f)