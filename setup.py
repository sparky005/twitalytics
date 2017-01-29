from setuptools import setup

setup(name="Twitalytics",
      version='0.1',
      description="Analyze people on twitter",
      url='none',
      author='sparky_005',
      author_email='sparky.005@gmail.com',
      license='MIT',
      packages=['twitalytics'],
      zip_safe=False,
      entry_points="""
      [console_scripts]
      twitalytics=twitalytics.twitalytics:main
      """,
      )
