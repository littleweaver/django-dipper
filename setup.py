from setuptools import setup, find_packages

__version__ = __import__('dipper').__version__


description = "Easy custom Django form rendering in Django and Jinja templates"


setup(
    name="django-dipper",
    version='.'.join([str(v) for v in __version__]),
    url="http://github.com/littleweaver/django-dipper",
    description=description,
    long_description=description,
    author='Little Weaver Web Collective, LLC',
    author_email='hello@littleweaverweb.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    platforms=['OS Independent'],
    install_requires=[
        'django>=1.7',
    ]
)
