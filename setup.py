import setuptools

setuptools.setup(
    name="codeBeatApi",
    version="0.0.1",
    author="Pedro Frattezi",
    author_email="pfrattezi@gmail.com.com",
    description="Flask Restful API for code monitoring",
    long_description_content_type="text/markdown",
    url="https://github.com/frattezi/codeBeatApi",
    packages=setuptools.find_packages(),
    install_requires=["Flask-RESTful==0.3.8", "psycopg2-binary==2.8.6"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
