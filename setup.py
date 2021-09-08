import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='image-shuffler',
    version='1.0.2',
    description='Split an image into n-pieces and shuffle it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/image-shuffler',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords= 'image shuffler slicer picture pieces',
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'opencv-python'],
    python_requires='>=3',
)