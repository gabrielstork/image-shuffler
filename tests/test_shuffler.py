from image_shuffler import Shuffler
import unittest


class TestShuffler(unittest.TestCase):
    def setUp(self) -> None:
        self.image = Shuffler('images/test_image.png')

    def test_original_image(self) -> None:
        self.assertRaises(ValueError, Shuffler, 'image')

    def test_pixel_loss(self) -> None:
        self.assertWarns(UserWarning, self.image.shuffle, (5, 5))

    def test_matrix_values(self) -> None:
        values = [
            (2, 2, 2),
            (2, -2),
            (2, 2.1),
            (2, 550),
        ]

        for value in values:
            self.assertRaises(ValueError, self.image.shuffle, value)

    def test_matrix_final_shape(self) -> None:
        self.image.shuffle((2, 2))
        shuffled_shape = self.image.shuffled.shape
        original_shape = self.image.original.shape

        self.assertEqual(shuffled_shape, original_shape)


if __name__ == '__main__':
    unittest.main()
