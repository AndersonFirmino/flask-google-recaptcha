
from setuptools import setup, find_packages
import flask_google_recaptcha

PACKAGE = flask_google_recaptcha

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='anderson.araujoprog@gmail.com',
    description="The working Google ReCaptcha implementation for Flask without Flask-WTF",
    long_description=PACKAGE.__doc__,
    url='https://github.com/AndersonFirmino/flask-google-recaptcha',
    download_url='http://github.com/AndersonFirmino/flask-google-recaptcha/tarball/master',
    py_modules=['flask_recaptcha'],
    include_package_data=True,
    install_requires=[
        "flask",
        "requests"
    ],
    keywords=['flask', 'recaptcha', "validate", "google"],
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
    zip_safe=False
)
