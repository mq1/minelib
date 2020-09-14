# mclib/server is a collection of minecraft server utilities
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

import os
import requests


class MinecraftServer:
    vanilla_version = ""

    def __init__(self, vanilla_version="release"):
        if vanilla_version == "release" or vanilla_version == "snapshot":
            self.fetch_latest_vanilla_version(vanilla_version)
        else:
            self.vanilla_version = vanilla_version

    # type can be "release" or "snapshot"
    def fetch_latest_vanilla_version(self, type):
        response = requests.get(
            "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        )
        self.vanilla_version = response.json()["latest"][type]

    def download(self, dir):
        response = requests.get(
            "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        )
        version_list = response.json()["versions"]
        version = next(
            lambda version: version["id"] == self.vanilla_version, version_list
        )

        response = requests.get(version["url"])
        server = response.json()["downloads"]["server"]["url"]

        response = requests.get(server["url"])
        open(
            os.path.join(dir, "/minecraft_server.${self.vanilla_version}.jar"), "wb"
        ).write(response.content)
