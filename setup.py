import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='image-shuffler',
    version='1.0.1',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    description='Split an image into n-pieces and shuffle it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/image-shuffler',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='.'),
    python_requires='>=3',
    install_requires=['numpy', 'opencv-python'],
)