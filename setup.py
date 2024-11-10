from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project has, e.g., `numpy`, `requests`, etc.
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz'
        ],
    },
    test_suite='pytest',  # or 'unittest' if using that for tests
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple math quiz game.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DeekshaPingalay/dsss_homework_2",  #repository link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",  #license
    ],
)
