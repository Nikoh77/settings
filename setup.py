from setuptools import setup, find_packages

setup(
    name="settings",
    version="1.0.6",
    description="A settings manager package",
    packages=find_packages(),
    author="Nikoh",
    author_email="nikoh@nikoh.it",
    url="https://github.com/Nikoh77",
    download_url="https://github.com/Nikoh77/settings.git",
    package_data={"settings": ["py.typed"]},
)
