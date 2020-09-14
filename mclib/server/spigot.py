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
from vanilla import MinecraftServer


class SpigotServer(MinecraftServer):
    def download(self, dir):
        response = requests.get(
            "https://cdn.getbukkit.org/spigot/spigot-${self.vanilla_version}.jar"
        )
        open(os.path.join(dir, "spigot-${self.vanilla_version}.jar"), "wb").write(response.content)
