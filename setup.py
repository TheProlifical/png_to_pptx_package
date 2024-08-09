from setuptools import setup, find_packages

setup(
    name="png_to_pptx",
    version="0.1",
    description="A tool to convert PNG images to a PPTX presentation with a 16:9 aspect ratio. _",
    author="Ahson",
    author_email="itsahson1978@gmail.com",
    url="https://github.com/TheProlifical/ppt-to-png_package",
    packages=find_packages(),
    install_requires=[
        "python-pptx",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

