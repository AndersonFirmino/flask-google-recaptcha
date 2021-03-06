from setuptools import setup
from setuptools import find_packages
import flask_google_recaptcha

PACKAGE = flask_google_recaptcha

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Flask-GoogleRecaptcha",
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='anderson.araujoprog@gmail.com',
    description="The working Google ReCaptcha implementation for Flask without Flask-WTF",
    long_description=long_description,
    long_description_content_type='text/markdown',
    setup_requires=['setuptools>=38.6.0'],
    url='https://github.com/AndersonFirmino/flask-google-recaptcha',
    packages=find_packages(),
    download_url='http://github.com/AndersonFirmino/flask-google-recaptcha/tarball/master',
    py_modules=['flask_recaptcha'],
    include_package_data=True,
    install_requires=[
        "flask",
        "jinja2"
    ],
    keywords=["flask", "recaptcha", "validate", "google", "google app engine", "not a robot"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=True
)
