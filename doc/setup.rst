===================
Setting up Jenkyns
===================

Install current development version
===================================

To install Jenkyns from source, use these commands:

.. code-block:: bash

    # Make sure you have the "python-virtualenv" package installed on your machine
    mkdir -p ~/bin ~/.config/jenkyns
    virtualenv --no-site-packages ~/.config/jenkyns/venv
    ~/.config/jenkyns/venv/bin/pip install \
        -e git+https://github.com/jhermann/jenkyns.git#egg=jenkyns
    ln -nfs ../.config/jenkyns/venv/bin/jenkyns ~/bin

Now try to call ``jenkyns -h`` which should print the command help. If the command is not found,
``~/bin`` might not yet be in your path, enter ``exec $SHELL -l`` and try to call ``jenkyns -h`` again.

On Windows, do something similar. ¯\\_(ツ)_/¯


Configuration
=============

* locations (map instances names to URLs)
* job classes (templates)

