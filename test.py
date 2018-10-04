import re
from git import Repo

repo = Repo("E:\\git\\pyproj")

assert not repo.bare
