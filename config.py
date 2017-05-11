"""
Common Keys used in all projects
"""

"""
All TVDB Specific keys
"""
DEFAULT_LANG = "en"


class TVDB_Info:

    BASE_URL = "http://thetvdb.com"
    API_KEY = "BC1C8A58B0FE28EC"
    GET_SERIES_ID = BASE_URL + "/api/GetSeries.php?seriesname={series_name}"
    GET_SERIES_INFO = BASE_URL + "/api/" + API_KEY + "/series/{series_id}/all/{series_lang}.zip"
    GET_SERVER_TIME = BASE_URL + "/api/Updates.php?type=none"
    GET_UPDATED_SERIES = BASE_URL + "/api/Updates.php?type=all&time={previous_time}"
    BANNERS_JPG = BASE_URL + "/banners/{img_path}"


class DDB_Info:
    HOST = "sanathr"
    DB = "dbs/TVShows"
    SUBSCRIPTION_ID = "d4cd038d-5113-4de1-9b6a-8dfbdbbe1f1c"

    URL = "https://" + HOST + ".documents.azure.com:443/"

    class Collection:
        TV_SHOWS = "/colls/US_TV_Shows"
        SERIES_INFO = "/colls/Series_Info"
        EPISODE_INFO = "/colls/Episode_Info"
        ACTOR_INFO = "/colls/Actor_Info"

    class Keys:
        PRIMARY = "LHi1WGIWdUlwwOPVVFdATbq7TvCzXKch5RI5tnV9igOkZke1DjcyviItxB6XASQTgxfmCQQprLHIxxlObi5Wxg=="
        SECONDARY = "JphjAQfLQVuRSCT6Ta7TCSjd8FKM7KQRLLYEkxm1yzN3rnT27pYfsguqcKutHYCKA1OcjhZrGkintvyvNu2b9Q=="

    CONN_STR = URL + ";AccountKey={key};"










