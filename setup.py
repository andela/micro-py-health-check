from distutils.core import setup # Describe module distribution to Distutils

setup(
    name='micro-py-health-check',
    packages=['micro-py-health-check'], # this must be the same as the name above
    version='0.1',
    description='A library to do rpc health checks on Python Services',
    author='Andela',
    author_email='devops@andela.com',
    url='https://github.com/andela/micro-py-health-check/tree/ft-create-micro-health-check-python-package',
    download_url='https://github.com/andela/micro-py-health-check/tree/ft-create-micro-health-check-python-package/archive/0.1.tar.gz',
    # I'll explain this in a second
    keywords=['testing', 'health checks', 'services', 'gRPC'], # arbitrary keywords
    classifiers=[],
)