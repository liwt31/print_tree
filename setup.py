import setuptools

with open('README.md', encoding='utf-8') as fin:
    long_description = fin.read()

setuptools.setup(
    name='print_tree2',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/liwt31/print_tree',
    license='MIT',
    author='Weitang Li',
    author_email='liwt31@163.com',
    description='Print trees'
)
