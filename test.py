import re
import os
from git import Repo

repo = Repo("E:\\git\\pyproj")

assert not repo.bare

repo = Repo("E:\\git")

assert not repo.bare

curdir = os.getcwd()

print (curdir)
    