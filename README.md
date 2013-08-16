# Jenkyns

## Overview
`jenkyns` is a command line tool that helps with the daily management of your 
Jenkins jobs, implemented using Python and with a focus on but not limited to
Python projects. The main goal is to automate configuration tasks and make
new project setups simple and fast, and systematic changes to a set of similar
jobs easy.

Unlike `jenkins-cli.jar` which uses JNLP to communicate, `jenkyns` relies on
the REST API and thus imposes less preconditions (if Jenkins works in your
browser, so will the tool).


## Jenkyns Concepts

locations: \[»instance«:]»jobname«


## Using jenkyns

commands: mkjob, cpjob, mvjob, rmjob


## Configuration
* locations (map instances names to URLs)
* job classes (templates)


## Contributing

To set up a working directory for the project, follow these steps:

    git clone https://github.com/jhermann/jenkyns.git
    cd jenkyns
    virtualenv --no-site-packages .
    . bin/activate
    pip install -r requirements.txt
    paver init

