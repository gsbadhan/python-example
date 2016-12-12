from setuptools import setup

setup(name='python-pkg',
      version='0.1',
      description='package for test',
      #url='http://github.com/storborg/funniest',
      author='gurpreet',
      author_email='gsingh@nimbuzz.com',
      license='nimbuzz',
      packages=['com','com.funniest'],
      include_package_data=True,
      zip_safe=False
      )