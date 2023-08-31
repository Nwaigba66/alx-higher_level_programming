#!/bin/bash
# this script takes a URL, sends a Get request along with a Header
curl -s -H $1 "X-School-User-Id: 98" 
