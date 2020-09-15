# minelib/server is a collection of minecraft server utilities
# Copyright (C) 2020  Manuel Quarneti

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import path
import requests
from . import server


class MinecraftServer(server.MinecraftServer):
    paper_version = ""

    def __init__(self, vanilla_version="release", paper_version="latest"):
        if vanilla_version == "release" or vanilla_version == "snapshot":
            self.fetch_latest_vanilla_version(vanilla_version)
        else:
            self.vanilla_version = paper_version

        if paper_version == "latest":
            self.fetch_latest_paper_version()
        else:
            self.paper_version = paper_version

    def fetch_latest_paper_version(self):
        response = requests.get(
            f"https://papermc.io/api/v1/paper/{self.vanilla_version}"
        )
        self.paper_version = response.json()["builds"]["latest"]

    def download(self, basedir):
        response = requests.get(
            f"https://papermc.io/api/v1/paper/{self.vanilla_version}/{self.paper_version}/download"
        )
        open(path.join(basedir, f"paper-{self.paper_version}.jar"), "wb").write(
            response.content
        )
