from setuptools import setup, find_packages

# from question_generation import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="question_generation",
    packages=find_packages(),
    version="0.1.0",
    url="https://github.com/patil-suraj/question_generation",
    license="MIT",
    author="Suraj Patil",
    author_email="surajp815@gmail.com",
    description="Question generation is the task of automatically generating questions from a text paragraph.",
    install_requires=["transformers==4.5.1", "nltk==3.2.5", "nlp==0.4.0", "torch==1.7.1", "sentencepiece==0.1.96", "protobuf==3.17.3"],
    python_requires=">=3.6",
    include_package_data=True,
    platforms="any",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)