# PyRankinity
This is a simple wraper around Rankinity V1 API (http://my.rankinity.com/api.en)

## Requirements
1. Rankinity API Token
2. Python 2.7+/3.0+ (note: 3.0+ is untested)

## Install
```python
pip install pyrankinity
```
or clone this repo and run

```python
python setup.py install
```

## Use

To start declare an api passing in access token

```python
import pyrankinity

api = pyrankinity
```

The method mappings:
  - projects - get_projects(self, **params)
  - competitors - get_competitors(self, project_id, **params)
  - keywords - get_keywords(self, project_id, **params)
  - keyword groups - get_keyword_groups(self, project_id, **params)
  - ranks - get_ranks(self, project_id, search_engine_id, **params)

**params can contain:
- shared
- search
- sort_ascending
- sort_property
- group

