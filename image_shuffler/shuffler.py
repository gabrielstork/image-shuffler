import random
import warnings
import cv2 as cv
import numpy as np


class Shuffler:
    def __init__(self, image_path: str) -> None:
        self.image = cv.imread(image_path)

        self.status = 'Original'
        self.y = self.image.shape[0]
        self.x = self.image.shape[1]

        self._pieces = []

    def _check_pixel_loss(self, x_missing: int, y_missing: int) -> None:
        new_x = self.x - x_missing
        new_y = self.y - y_missing

        if (x_missing + y_missing) > 0:
            warnings.warn(
                'Splitting images into non-integer intervals causes pixel loss. '
                f'Original Shape: ({self.x}, {self.y}) '
                f'New Shape: ({new_x}, {new_y})',
                stacklevel=3
            )

    def _split(self, x: int, y: int, x_list: list, y_list: list) -> None:
        for x_n, x_piece in enumerate(x_list):
            for y_n, y_piece in enumerate(y_list):
                self._pieces.append(
                    self.image[y_n * y:y_piece, x_n * x:x_piece]
                )

    def _generate_image(self, cols: int) -> None:
        chunks = [
            np.vstack(piece) for piece in zip(*[iter(self._pieces)] * cols)
        ]
        self.image = np.hstack(np.array(chunks, dtype=np.uint8))
        self.status = 'Shuffled'

    def shuffle(self, matrix: tuple) -> None:
        x = int(self.x / matrix[0])
        x_missing = self.x - (x * matrix[0])
        x_list = list(range(x, self.x + 1, x))

        y = int(self.y / matrix[1])
        y_missing = self.y - (y * matrix[1])
        y_list = list(range(y, self.y + 1, y))

        self._check_pixel_loss(x_missing, y_missing)
        self._split(x, y, x_list, y_list)
        random.shuffle(self._pieces)

        self._generate_image(matrix[1])

    def show(self) -> None:
        cv.imshow(self.status, self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path: str) -> None:
        cv.imwrite(path, self.image)
