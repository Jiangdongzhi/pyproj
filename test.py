import re
from git import Repo

repo = Repo("/home/dongzhi/workspace/pyproj")

assert not repo.bare
