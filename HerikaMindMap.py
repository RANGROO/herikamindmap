import os, sys
import re
import time 
import chromadb
import argparse
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

parser = argparse.ArgumentParser(description="Extract and save an IPv4 address")
parser.add_argument("--ip", type=str, help="Address of ChromaDB (e.g. http://192.168.86.123:8000/)")
args = parser.parse_args()

#Helps import the files for ChromaViz
base_dir = '.'
if hasattr(sys, '_MEIPASS'): # or, untested: if getattr(sys, 'frozen', False):
    base_dir = os.path.join(sys._MEIPASS)
    
#Strips the IP address of either the --ip arg or ask the user to enter it. 
#Will just use the IP address if passed through the --ip arg
if args.ip:
    ipaddr = args.ip
    ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    match  = re.search(ipv4_pattern, ipaddr )
else:
    ipaddr = input("Enter the CHROMADB REST-API from the DwemerDistro (e.g. http://192.168.86.123:8000/):")
    ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    match  = re.search(ipv4_pattern, ipaddr )

if match:
    #Extract and store the matched IPv4 address in the ipaddr variable
    ipaddr = match.group()
    
    #Starts the HerikaMindMap server
    chroma_client = chromadb.HttpClient(host= ipaddr, port=8000)
    collection = chroma_client.get_collection("herika_memories")
    visualize_collection(collection)

else:
    print("Invalid address format. Exiting.")
    time.sleep(5)

