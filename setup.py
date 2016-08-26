from setuptools import setup, find_packages

# parse requirements
req_lines = [line.strip() for line in open(
    'requirements.txt').readlines()]
install_reqs = list(filter(None, req_lines))

setup(
    name="pdfdiff",
    version="0.1",
    author="Nitin Kumar",
    author_email="vnitinv@rediffmail.com",
    description=("Print difference between 2 pdf on console"),
    license="Apache 2.0",
    keywords="automation python framework",
    url="http://www.github.com/vnitinv/pdfdiff",
    install_requires=install_reqs,
    py_modules=['pdfdiff'],
    entry_points={
        'console_scripts': [
            'pdfdiff=pdfdiff:start',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
