from setuptools import setup

setup(
    name='myshop',
    version='1.0',
    description='OpenShift App - LFC',
    author='Kamal bin Mustafa',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.1.4',
        'django-lfs',
        'django-lfstheme',
        'Pillow',
    ],
)
