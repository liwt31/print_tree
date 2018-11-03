import setuptools

with open("README.md", "rb") as fin:
    long_description = fin.read().decode("utf-8")

setuptools.setup(
    name="print-tree2",
    version="0.9.9",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liwt31/print-tree",
    license="MIT",
    author="Weitang Li",
    author_email="liwt31@163.com",
    description="Print trees",
)
