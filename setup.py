from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pyeventbus3',
      version='0.9',
      description='A Python EventBus',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
      ],
      keywords='python eventbus with threading and concurrency support',
      url='https://github.com/FlavienVernier/pyeventbus',
      author='Nanda Bhat, Flavien Vernier',
      author_email='n89nanda@gmail.com, flavien.vernier@gmail.com',
      license='MIT',
      packages=['pyeventbus3'],
      install_requires=[
          'gevent',
      ],
      include_package_data=True,
      zip_safe=False)
