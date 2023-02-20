from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Sentiment_analaysis_using_biRNN"
AUTHOR_USER_NAME = "deepakthakur-92"
SRC_REPO = "Sentiment_analaysis"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="1.0.0",
    author=AUTHOR_USER_NAME,
    description="A small package for MLflow app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/deepakthakur-92/Sentiment_analaysis_using_biRNN",
    author_email="deepak2009thakur @gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
