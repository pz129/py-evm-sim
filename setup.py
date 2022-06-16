from setuptools import setup, find_packages

# install_requires = [
#   'py-evm @ git+ssh://git@github.com/ethereum/py-evm@v0.5.0-alpha.3',
# ]

setup(
    name='py-evm-sim',
    packages=find_packages(),
    url='https://github.com/pz129/py-evm-sim',
    description='Robust simulation and testing suite for EVM compatible smart contractsc',
    long_description=open('README.md').read(),
    install_requires=[
        "requests==2.7.0",
         'py-evm @ git+ssh://git@github.com/ethereum/py-evm@v0.5.0-alpha.3#egg=py-evm',
        ],
    include_package_data=True,
)