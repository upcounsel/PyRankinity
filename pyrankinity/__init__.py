import requests
import json,datetime

class PyRankinityException(Exception):
  pass

class PyRankinity(object):
  _V1_URL = "http://my.rankinity.com/api/v1"

  def __build_params(self, **params):
    param_values = ['sort_ascending','search','sort_property','shared','group']
    payload = {'token': self.access_token}
    for p in param_values:
      if p in params:
        payload[p] = params[p]
    return payload

  def get_projects(self, **params):
    payload = self.__build_params(**params)
    response = requests.get("{0}/projects.json".format(self._V1_URL), params=payload)
    return PyRankinity.__handle_response(response)['projects']

  def get_competitors(self, project_id, **params):
    payload = self.__build_params(**params)
    response = requests.get("{0}/projects/{1}/competitors.json".format(self._V1_URL, project_id), params=payload)
    return PyRankinity.__handle_response(response)['competitors'] 

  def get_keywords(self, project_id, **params):
    payload = self.__build_params(**params)
    response = requests.get("{0}/projects/{1}/keywords.json".format(self._V1_URL, project_id), params=payload)
    return PyRankinity.__handle_response(response)['keywords']

  def get_keyword_groups(self, project_id, **params):
    payload = self.__build_params(**params)
    response = requests.get("{0}/projects/{1}/groups.json".format(self._V1_URL, project_id), params=payload)
    return PyRankinity.__handle_response(response)['groups']

  def get_ranks(self, project_id, search_engine_id, **params):
    payload = self.__build_params(**params)
    response = requests.get("{0}/projects/{1}/search_engines/{2}/ranks.json".format(self._V1_URL, project_id, search_engine_id), params=payload)
    return PyRankinity.__handle_response(response)['ranks']

  def __init__(self, access_token):
    self.access_token = access_token

  @staticmethod
  def __handle_response(response):
    if response.status_code == 200:
      return json.loads(response.text)
    else:
      raise PyRankinityException(response.text)

  @staticmethod
  def unixtime_to_datetime(unixtime):
    return datetime.datetime.utcfromtimestamp(u)