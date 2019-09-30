import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="htmltojpg",
    version="0.0.1",
    author="Andrew Redmond",
    author_email="andrewpredmond@gmail.com",
    description="convert html page into jpg image.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user/repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
        'imgkit',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Optional
        'console_scripts': [
            'htmltojpg=src.html_to_jpeg:html_to_jpeg',
        ],
    },
)