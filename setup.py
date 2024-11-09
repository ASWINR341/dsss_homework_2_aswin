from setuptools import setup, find_packages

setup(
    name="dsss_homework_2_aswin",
    version="1.0.0", 
    author="Aswin Ramachandran",
    description="This a math quiz program, to check you calculation ability",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
)
