import pyrankinity


ACCESS_TOKEN = '049d62336ad1dc050e78484733d57af2'

api = pyrankinity.PyRankinity(ACCESS_TOKEN)

projects = api.get_projects()
competitors = api.get_competitors(projects[0]["id"])
keywords = api.get_keywords(projects[0]["id"])
keyword_groups = api.get_keyword_groups(projects[0]["id"])
ranks = api.get_ranks(projects[0]["id"],projects[0]['visibility_infos'][0]['search_engine_id'])