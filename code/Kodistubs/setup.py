from io import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import kodistubs_meta

with open('README.rst', encoding='utf-8') as fo:
    long_descr = fo.read()

setup(
    name='Kodistubs',
    version=kodistubs_meta.VERSION,
    py_modules=['xbmc', 'xbmcaddon', 'xbmcgui', 'xbmcplugin', 'xbmcvfs'],
    install_requires=['typing'],
    zip_safe=False,
    description='Stub modules that re-create Kodi Python API',
    long_description=long_descr,
    author=kodistubs_meta.AUTHOR,  # The new Kodistubs have been generated from scratch
    author_email=kodistubs_meta.EMAIL,
    url='https://github.com/romanvm/Kodistubs',
    license='GPLv3',
    keywords="kodi documentation inspection",
    classifiers=[
        'Environment :: Plugins',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
