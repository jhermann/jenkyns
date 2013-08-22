# Jenkyns

_Keywords:_ jenkins, devops, automation, build pipeline, continuous delivery


## Overview
`jenkyns` (ˈdʒɛŋkaɪnz) is a command line tool that helps with the daily
management of your Jenkins jobs, implemented using Python and with a
focus on but not limited to Python projects. The main goal is to automate
configuration tasks and make new project setups simple and fast, and
systematic changes to a set of similar jobs easy.

Unlike `jenkins-cli.jar` which uses JNLP to communicate, `jenkyns` relies on
the REST API and thus imposes less preconditions (if Jenkins works in your
browser, so will the tool).


## Documentation

The documentation for the current GitHub master source is located at
[github.io](http://jhermann.github.io/jenkyns/).
There you will find instructions on how to
[install](http://jhermann.github.io/jenkyns/setup.html) and
[use](http://jhermann.github.io/jenkyns/usage.html)
the `jenkyns` tool.


## Contributing

Jenkyns is written in [Python](http://www.python.org/),
and the documentation is generated using [Sphinx](https://pypi.python.org/pypi/Sphinx).
[Paver](https://pypi.python.org/pypi/Paver) is used to build and manage the project.

To set up a working directory, follow these steps:

    git clone https://github.com/jhermann/jenkyns.git
    cd jenkyns
    virtualenv --no-site-packages .
    . bin/activate
    pip install -r requirements.txt
    paver init

Jenkyns can also be found on [PyPI](https://pypi.python.org/pypi/jenkyns)
and [Ohloh](https://www.ohloh.net/p/jenkyns).


## License

Jenkyns is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html), see LICENSE for details.


## Similar Projects

**Python**

* *API centric*
  * [jenkins-webapi](https://github.com/gvalkov/jenkins-webapi)
  * [jenkinsapi](https://github.com/salimfadhley/jenkinsapi)
  * [python-jenkins](https://launchpad.net/python-jenkins)
* *Tool centric*
  * [autojenkins](https://github.com/txels/autojenkins)
  * [jenkins-job-builder](https://github.com/openstack-infra/jenkins-job-builder)
  * [jenkins-autojobs](https://github.com/gvalkov/jenkins-autojobs)


**Clojure**

* [jenkins](https://github.com/owainlewis/jenkins)

