import os, sys
import chromadb
import onnxruntime
import tokenizers
from chromadb.telemetry import posthog
from chromadb.api import segment
from chromadb.db import impl
from chromadb.db.impl import sqlite
from chromadb import migrations
from chromadb.migrations import embeddings_queue
from chromadb.api import fastapi
from chromaviz import visualize_collection


base_dir = '.'
if hasattr(sys, '_MEIPASS'): # or, untested: if getattr(sys, 'frozen', False):
    base_dir = os.path.join(sys._MEIPASS)
    
chroma_client = chromadb.HttpClient(host="192.168.86.123", port=8000)
collection = chroma_client.get_collection("herika_memories")
visualize_collection(collection)

