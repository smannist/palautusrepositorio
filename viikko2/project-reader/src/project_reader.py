from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dictionary = toml.loads(content, _dict=dict)

        name = content_dictionary.get("tool", {}).get("poetry",{}).get("name")
        description = content_dictionary.get("tool", {}).get("poetry", {}).get("description")
        dependencies = content_dictionary.get("tool", {}).get("poetry", {}).get("dependencies")
        dev_dependencies = content_dictionary.get("tool", {}).get("poetry", {}).get("dev-dependencies")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
