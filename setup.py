from setuptools import setup, find_packages

setup(
    name="price-track-pro-ecommerce-20260507_200423",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'price=price:main',
        ],
    },
)
