from setuptools import setup

setup(
    name='PySphericalStats3D',
    version='2.1',
    packages=['PySphericalStats3D', 'PySphericalStats3D.util', 'PySphericalStats3D.manager', 'PySphericalStats3D.manager.graphs'],
    url='https://github.com/pablogarguez/PySphericalStats3D',
    license='Apache 2.0',
    author='Pablo García Rodríguez',
    author_email='pablogarguez@gmail.com',
    description='Spherical Statistcis Analysis', install_requires=['matplotlib', 'scipy', 'numpy']
)
