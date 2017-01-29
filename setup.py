from setuptools import setup

# requirements
install_requires = ["tweepy"]

setup(name="Twitalytics",
      version='0.1',
      description="Analyze people on twitter",
      url='none',
      author='sparky_005',
      author_email='sparky.005@gmail.com',
      license='MIT',
      packages=['twitalytics'],
      zip_safe=False,
      install_requires = install_requires,
      entry_points="""
      [console_scripts]
      twitalytics=twitalytics.twitalytics:main
      """,
      )
