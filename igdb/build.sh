python3 setup.py sdist
python3 setup.py bdist_wheel
python3 -m pip install dist/mypackage-0.1.5.tar.gz  # Replace with the actual version number
# or
#pip install dist/mypackage-0.1-py3-none-any.whl  # Replace with the actual version number

