from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict= toml.loads(content)
        dep = content_dict['tool']['poetry']['dependencies'].keys()
        deplist = ""
        for key in dep:
            deplist = deplist + str(key) + ", "
        deplist = deplist[0:len(deplist)-2]
        depdev = content_dict['tool']['poetry']['dev-dependencies'].keys()
        depdevlist = ""
        for key in depdev:
            depdevlist = depdevlist + str(key) + ", "
        depdevlist = depdevlist[0:len(depdevlist)-2]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("TEST", "Test description", [], [])
        return Project(content_dict['tool']['poetry']['name'],content_dict['tool']['poetry']['description'],[deplist],[depdevlist])
