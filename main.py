"""
Main Class
"""
import logging
import os

from utils import init_logger, rollback_log
from pydocumentdb.document_client import DocumentClient
from config import DDB_Info, TVDB_Info


class BreakingTv(object):

    def __init__(self, episodes=[]):
        self.episodes = episodes
        self.docdb_client = None
        self.log_path = os.path.join(os.getcwd(), "breakingtv.log")
        rollback_log(self.log_path)
        init_logger(self.log_path)

    def connect_to_ddb(self):
        auth = {"masterKey": DDB_Info.Keys.PRIMARY}
        self.docdb_client = DocumentClient(DDB_Info.URL, auth)
        logging.info("Connected Successfully to DDB")

    def get_documents(self, collection):
        documents = self.docdb_client.ReadDocuments(DDB_Info.DB + collection)
        for doc in documents:
            logging.info(doc['id'])


def main():
    breaking_tv = BreakingTv()
    breaking_tv.connect_to_ddb()
    breaking_tv.get_documents(DDB_Info.Collection.TV_SHOWS)


if __name__ == "__main__":
        main()



