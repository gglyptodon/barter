import setuptools

setuptools.setup(
    name='barter',
    version='0.0.1',
    packages=setuptools.find_packages(include=['barter', 'barter.*'], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    license='GNU Lesser General Public License v3.0',
    scripts=['barter_text.py', 'barter_csv.py'],
    install_requires=['Pillow', 'treepoem']
)