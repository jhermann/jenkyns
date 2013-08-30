.. jenkyns documentation: setup

   Copyright © 2013 Jürgen Hermann
  
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
  
     http://www.apache.org/licenses/LICENSE-2.0
  
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

To find out your *API Token*, after logging into your Jenkins instance,
click on the account name in the top right corner,
and then on *Configure* in the sidebar menu
(bringing you to an URL like `http://jenkins.example.com/hudson/user/»username«/configure`).
Click on the *Show API Token…* button in the *API Token* section,
subsequently copy the displayed value … **TODO**.

