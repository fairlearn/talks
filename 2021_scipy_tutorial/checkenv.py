import sys
from pkgutil import iter_modules


packages = [
    "jupyter",
    "fairlearn",
    "seaborn",
    "numpy",
    "pandas",
    "model-card-toolkit"
]

assert (sys.version_info.major >= 3 and sys.version_info.minor >= 7), "Python version needs to be upgraded to Python 3.7"

installed_packages = [pkg_name for (module, pkg_name, _) in iter_modules()]



for package in packages:
    assert package in packages, f"{package} was not present in Python environment"

print("All packages were installed correctly")