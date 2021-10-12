# image-shuffler

Split an image into n-pieces and shuffle it.

![Comparison](https://raw.githubusercontent.com/gabrielstork/image-shuffler/main/images/comparison.png)

## Download

You can simply:

```sh
pip install image-shuffler
```

Or you can also:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/image-shuffler.git
cd image-shuffler
pip install -r requirements.txt
```

## How to use

First you need to import the `Shuffler` class.

```python
from image_shuffler import Shuffler
```

Then, instantiate it passing a valid path of an image as its argument.

```python
image = Shuffler('lenna.png')
```

Now to actually shuffle it, you need to use `shuffle()` method. The matrix defines the number of pieces that will be in `x` and `y`, in this case, there will be a total of 16 shuffled pieces (you can see it in the image on the top of this file).

```python
image.shuffle(matrix=(4, 4))
```

You can take a look at the image, using this method a new window will pop up.

```python
image.show()
```

No arguments are needed to save the image. It will be saved in the same place and, in this case, with `shuffled_lena.png` as its name.

```python
image.save()
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)
