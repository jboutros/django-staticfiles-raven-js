from distutils.core import setup
import os

# Stolen from django-statucfiles-jquery which was stolen from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('ravenjs'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len('ravenjs/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name='django-staticfiles-raven-js',
    version=open("./VERSION").read(),
    description='ravenjs meets Django staticfiles',
    author='Chad Masso',
    author_email='chadm@indeed.com',
    packages=packages,
    package_data={'ravenjs': data_files},
)
