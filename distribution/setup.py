import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bookforyou_Bohdan_Mykhayliv", # Replace with your own username
    version="1.1",
    author="Bohdan Mykhayliv",
    author_email="bohdan.mykhailiv@ucu.edu.ua",
    description="Function returns user dataframe with books which suit to user`s criterions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmykhaylivvv/mini_project_first_semester",
    packages=['book_for_you'],
    package_dir = {'book_for_you': 'book_for_you'},
    package_data = {'book_for_you': ['data/*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)