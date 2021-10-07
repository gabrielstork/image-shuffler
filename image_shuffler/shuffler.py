import random
import warnings
import cv2 as cv
import numpy as np


class Shuffler:
    def __init__(self, image: str) -> None:
        self.original = cv.imread(image)
        self.shuffled = self.original.copy()

        self.x = self.original.shape[1]
        self.y = self.original.shape[0]

        self._pieces = []

    def _check_argument(self, matrix: tuple) -> None:
        if len(matrix) != 2 or not all(isinstance(x, int) for x in matrix):
            raise ValueError(
                'matrix must be 2-dimensional containing only integer numbers'
            )
        elif min(matrix) <= 0:
            raise ValueError('matrix values must be greater than 0')
        elif matrix > (self.x, self.y):
            raise ValueError('number of splits greater than pixels') 

    def _check_pixel_loss(self, x_missing: int, y_missing: int) -> None:
        new_x = self.x - x_missing
        new_y = self.y - y_missing

        if (x_missing + y_missing) > 0:
            warnings.warn(
                'Splitting images into non-integer intervals causes pixel '
                f'loss. Original Shape: ({self.x}, {self.y}) New Shape: '
                f'({new_x}, {new_y})',
                stacklevel=2,
            )

    def _split(self, x: int, y: int, x_list: list, y_list: list) -> None:
        if len(self._pieces) > 0:
            self._pieces.clear()

        for x_n, x_piece in enumerate(x_list):
            for y_n, y_piece in enumerate(y_list):
                self._pieces.append(
                    self.original[y_n * y:y_piece, x_n * x:x_piece]
                )

    def _generate_image(self, cols: int) -> None:
        chunks = [
            np.vstack(chunk) for chunk in zip(*[iter(self._pieces)] * cols)
        ]
        self.shuffled = np.hstack(np.array(chunks, dtype=np.uint8))

    def shuffle(self, matrix: tuple) -> None:
        self._check_argument(matrix)

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
        cv.imshow('Image', self.shuffled)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def save(self, path: str) -> None:
        cv.imwrite(path, self.shuffled)
