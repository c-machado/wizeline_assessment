# How to set up?
This project has been built using Python and Pytest-BDD. All the expected behaviours
have been documented using the Gherkin language.


## What do you need?
In order to set up this project you required:

1. An up-to-date version of Python 3
1. pipenv and virtualenv, to manage the dependencies and the virtual environment
1. Install python with pyenv, so you can manage the installed versions
1. Install dependencies store in the pipfile.

If you're unsure which Python version you have in your machine, please run the following command in your terminal:
```
$ python --version
```

## How to install python with pyenv?
1. Check if pyenv is installed
```
$ pyenv --version
```
If you do not have it, then click [here](https://github.com/pyenv/pyenv#readme) and follow the instructions.

2. Check all versions of python installed
```
$ pyenv versions
```
3. Check list of versions of python available
```
$ pyenv install --list
```
4. Install the version needed
```
$ pyenv install 3.9.6
```
If you are on MacOS Big Sur, you may need to complete an additional configuration:

4.1. Install required dependencies
```
$ brew install zlib
$ export LDFLAGS="-L/usr/local/opt/zlib/lib"
$ export CPPFLAGS="-I/usr/local/opt/zlib/include
$ brew install readline xz
```

4.2. Align command-line tools
```
1. Open Xcode
2. Go to Preference > Locations
3. Select the right version of command-line tools
```

4.3. Install Python
```
$ CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include
-I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib
-L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install 3.9.6
```
5. Check the version installed is on the installed versions of python
```
$ pyenv versions
```
6. Set the installed version as the python to use by your system
```
$ pyenv global 3.9.6
$ pyenv shell 3.9.6
```
7. Install pyenv-virtualenv to manage the virtual environment

Click [here](https://github.com/pyenv/pyenv-virtualenv) to complete pyenv-virtualenv installation.

pip [here](https://phoenixnap.com/kb/install-pip-mac)

## How to install the dependencies?
Note: Always use a virtual environment to manage your packages and dependencies
1. Go to folder’s project
1. Create or activate an existing virtual environment.
```
$ pyenv virtualenv environment-name
```
The environment should be activated automatically (once you added the variable pyenv-virtualenv):
```
$ pyenv versions
```
Otherwise, activate the environment manually:
```
$ pyenv shell environment-name
```
8. Install pip [here] (https://pip.pypa.io/en/stable/installation/)


9. Install pipenv, in order to manage your pipfile
```
pip install pipenv
```
10. Install the environment with the modules defined in the pipfile
```
$ pipenv install
```

## How to run tests?
1. Run tests in a specific file
```
$ pipenv run python3 -m pytest
```
Within the test file, you need to specify the feature file and the scenario to run, e.g:
```
@scenarios("../features/file_name.feature")
```
1. Run tests for a specific tag
```
$ pipenv run python3 -k pytest “env-mac”
```

## How to run tests in parallel?

1. Install pytest-xdist
```
$ pipenv install pytest-xdist
```
1. Now to run tests in parallel, you'll need to use the -n and then you provide the number of threads you want to run
```
$ pipenv run python3 -m pytest tests/step_defs/download_chrome_steps.py -n 3
```

## How to run tests in docker container?

1. Create a Dockerfile in the root. The files to copy to the docker container need to be moved folder by folder in order to keep the project’s structure.
```
FROM python:3.9.6-buster

# Install tini.
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini"]

# Install OS dependencies.
RUN apt-get update -qqy \
  && apt-get -qqy install graphviz

# Install browsers.
# Chrome
# ARG CHROME_VERSION="google-chrome-stable=92.0.4515.107"
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}

# TODO: add firefox

# Install python dependencies.
WORKDIR /tests
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy test drives.
WORKDIR /tests/bin/linux
COPY /tests/bin/linux /tests/bin/linux
ENV PATH="/:${PATH}"
ENV PATH="/tests/bin/linux:${PATH}"

# Copy test source code.
WORKDIR /tests
COPY tests/consts/* consts/
COPY tests/features/* features/
COPY tests/pages/* pages/
COPY tests/step_defs/* step_defs/
COPY tests/step_defs_mobile/* step_defs_mobile/
COPY tests/__init__.py .
COPY tests/conftest.py .
COPY tests/pytest.ini .
COPY tests/run_tests.sh .

#RUN echo $(ls -laR /tests/)

# Reports.
# VOLUME [ "reports" ]

# Run the test command.
CMD ["/tests/run_tests.sh"]
```

2. To build the container, run the compile.sh
```
#!/usr/bin/env bash

pip freeze > requirements.txt

# TODAY=$(date +'%Y%m%d')

docker build . --tag keyword/linux:latest

# --no-cache --progress plain
```

3. To run tests, execute run_tests.sh
```
#!/usr/bin/env bash

printf "STARTING DOCKER TEST:\n"

pytest tests/ -m "press" --html=reports/blog/press.html
```

## How to see pytest help?
```
$ pytest -h
```
## Any troubles?

If you run into any issues while trying to execute this suite, please feel
free to contact me at **dcmachadou@gmail.com**, I'll be happy to take a look at it.

Thank you!
:sunglasses:

### How to do authentication

1. Terminal should ask for an user, use your hugeinc username, e.g mguevara
2. Terminal should ask for a password, to generate it:
   - Go to https://github.hugeinc.com/settings/developers
   - Go to Personal access tokens
   - Click on Generate new token
   - Select **all** the main options of the list
   - Click on Generate token
   - Copy and save the token, even if you only have to enter the toke once. You won't be able to see it again. If you lose it is necessary to generate a new one.
   - Use the token as the password asked by the terminal
