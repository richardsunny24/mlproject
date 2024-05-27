#__init__.py is required because in setup.py the packages=find_packages() will look for folders iwth init.py and
# conisder it as a oackages/module and te=hen we can import this module.
# project deleopment happens within this init.py file and every folder we create should have this init.py file.