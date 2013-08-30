# -*- coding: utf-8 -*-
""" (Python) Jenkins Tools.

    jenkyns is a command line tool that helps with the daily management
    of your Jenkins jobs.
"""
# Copyright © 2013 Jürgen Hermann
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def pkg_info():
    """Return project information for setuptools."""
    try:
        doc = __doc__.decode("UTF-8")
    except (AttributeError, UnicodeError):
        doc = __doc__ # Python3, or some strangeness

    return dict(
    )

