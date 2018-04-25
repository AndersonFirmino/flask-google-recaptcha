# Flask Google ReCaptcha

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

The Working Google ReCaptcha implementation for Flask without Flask-WTF.

Can also be used as standalone

---

## Install
    pip install Flask-GoogleReCaptcha

    # or

    pip install git+https://github.com/AndersonFirmino/flask-google-recaptcha.git

    If you are using pipenv
    pipenv install Flask-GoogleReCaptcha


This implementation is pure and has no dependencies from third parties. Works in both Python2 and Python3.
You can use it in any flask project.

Has Google App Engine (GAE) support!


# Usage

### Implementation view.py

    from flask import Flask
    from flask_google_recaptcha import GoogleReCaptcha

    app = Flask(__name__)
    recaptcha = GoogleReCaptcha(app=app)

    # or

    recaptcha = GoogleReCaptcha()
    recaptcha.init_app(app)


### In your template: **{{ recaptcha }}**

Inside of the form you want to protect, include the tag: **{{ recaptcha }}**

It will insert the code automatically


    <form method="post" action="/submit">
        ... your field
        ... your field

        {{ recaptcha }}

        [submit button]
    </form>




### Verify the captcha

In the view that's going to validate the captcha

    from flask import Flask
    from flask_google_recaptcha import GoogleReCaptcha

    app = Flask(__name__)
    recaptcha = GoogleReCaptcha(app=app)

    @route("/submit", methods=["POST"])
    def submit():

        if recaptcha.verify():
            # SUCCESS
            pass
        else:
            # FAILED
            pass


Remember to set SITE_KEY and SECRET_KEY if not it does not appear!

## Api

**reCaptcha.__init__(app, site_key, secret_key, is_enabled=True)**

**reCaptcha.get_code()**

Returns the HTML code to implement. But you can use
**{{ recaptcha }}** directly in your template

**reCaptcha.verfiy()**

Returns bool

## In Template

Just include **{{ recaptcha }}** wherever you want to show the recaptcha


## Config

Flask-ReCaptcha is configured through the standard Flask config API.
These are the available options:

**RECAPTCHA_ENABLED**: Bool - True by default, when False it will bypass validation

**RECAPTCHA_SITE_KEY** : Public key

**RECAPTCHA_SECRET_KEY**: Private key

The following are **Optional** arguments.

**RECAPTCHA_THEME**: String - Theme can be 'light'(default) or 'dark'

**RECAPTCHA_TYPE**: String - Type of recaptcha can be 'image'(default) or 'audio'

**RECAPTCHA_SIZE**: String - Size of the image can be 'normal'(default) or 'compact'

**RECAPTCHA_TABINDEX**: Int - Tabindex of the widget can be used, if the page uses tabidex, to make navigation easier. Defaults to 0

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""
    RECAPTCHA_THEME = "dark"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "compact"
    RECAPTCHA_RTABINDEX = 10

---

Anderson Araujo (coderpy) :snake:
