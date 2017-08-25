from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import nltk

# requirements
install_requires = ["tweepy", "nltk", "dill", "pandas", "textblob", "scikit-learn==0.18.1", "scipy"]

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        print("Install in dev mode")
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print("Installing in real mode")
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('wordnet')
        install.run(self)

setup(name="Twitalytics",
      version='0.1',
      description="Analyze people on twitter",
      url='none',
      author='sparky_005',
      author_email='sparky.005@gmail.com',
      license='MIT',
      packages=['twitalytics'],
      package_data={'': ['tweet_emotion_classifier.pkl']},
      zip_safe=False,
      install_requires = install_requires,
      entry_points="""
      [console_scripts]
      twitalytics=twitalytics.twitalytics:main
      """,
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      },
      )



