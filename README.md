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

## Example

```python
from image_shuffler import Shuffler
```

```python
image = Shuffler('lenna.png')

# Splitting the image into 16 pieces, and shuffling it.
image.shuffle((4, 4))

# Seeing the image.
image.show()

# Saving the image.
image.save('lenna_shuffled.png')
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)
