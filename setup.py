from setuptools import setup

setup(
    name="settings",
    version="1.0.7",
    description="A settings manager package",
    url="https://github.com/Nikoh77/settings",
    author="Nikoh",
    author_email="nikoh@nikoh.it",
    packages=["settings"],
    package_data={"settings": ["py.typed"]},
    install_requires=[
        "configparser",
        "ipaddress",
        "json",
        # other dependencies here
    ],
    python_requires=">=3.6",
)
