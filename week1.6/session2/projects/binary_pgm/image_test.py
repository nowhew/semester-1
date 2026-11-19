from image import Image

def test_pbm_bin():
    image = Image()
    image.read_pgm("../../images/raw_coins.pgm")

    image.write_pgm("./coins.pgm")

if __name__ == "__main__":
    test_pbm_bin()