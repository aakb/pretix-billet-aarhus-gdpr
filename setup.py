import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1, interactive=False)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-billet-aarhus-gdpr',
    version='1.0.0',
    description='GDPR for billet.aarhus.dk',
    long_description=long_description,
    url='https://github.com/aakb/pretix-billet-aarhus-gdpr.git',
    author='Mikkel Ricky',
    author_email='rimi@aarhus.dk',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_billetaarhusgdpr=pretix_billetaarhusgdpr:PretixPluginMeta
""",
)
