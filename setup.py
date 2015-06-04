from setuptools import setup

setup(name='PyRankinity',
      version='0.1',
      description='Rankinity API Wrapper - See http://my.rankinity.com/api.en',
      author='UpCounsel',
      author_email='brad@upcounsel.com',
      url='https://www.github.com/upcounsel/pyrankinity',
      packages=['pyrankinity'],
      install_requires=[
          'requests',
      ],
      license='MIT'
     )