from setuptools import setup
from setuptools import find_packages

install_requires = [
    'Keras',
    'recurrentshop'
]

setup(
      name='seq2seq',
      version='1.0.0',
      description='Apprentissage de séquence à séquence avec des réseaux neuronaux',
      author='Mimboure Yara',
      author_email='dmsy2014@gmail.com',
      url='https://github.com/MimboureYara/seqseq',
      license='None',
      install_requires=install_requires,
      packages=find_packages(),
      dependency_links=['git+git://github.com/datalogai/recurrentshop.git']
)
