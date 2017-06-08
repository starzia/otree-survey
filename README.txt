PREREQUISITES
-------------

* Python 3.6
* pip


RUNNING IT
----------

    $ pip3 install virtualenv
    $ virtualenv virtualenv
    $ . virtualenv/bin/activate
    $ pip3 install otree-core
    $ otree startproject oTree
    $ cd oTree
    $ otree resetdb
    $ otree runserver

or

    $ OTREE_PRODUCTION=1 otree runserver 0.0.0.0:8000
