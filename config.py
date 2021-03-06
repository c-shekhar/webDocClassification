from pymongo import MongoClient
import redis

HOST_NAME = "localhost"
PORT_NAME = 27017
CLIENT_OBJECT = MongoClient(HOST_NAME,PORT_NAME)
DATABASE_NAME = "webDocClassification"
db = CLIENT_OBJECT[DATABASE_NAME]
FEEDS_COLLECTION_NAME = "feedsInfo"
DATA_COLLECTION_NAME = "htmlInfo"
BLOCK_COLLECTION_NAME = "blockInfo"

STATEMENT_LENGTH = 13
MAXIMUM_CHARACTERS = 80
BOILER_PLATE_THRESHOLD = 30

