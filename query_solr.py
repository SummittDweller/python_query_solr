# Python with JSON
# Lifted from https://cwiki.apache.org/confluence/display/solr/Using+Python

# JSON is a more robust response format, but you will need to add a Python package in order to use it. 
# At a command line, install the simplejson package like this:
# $ sudo easy_install simplejson

# Once that is done, making a query is nearly the same as before. 
# However, notice that the wt query parameter is now json, and the response is now digested by simplejson.load().

from urllib2 import *
import simplejson
connection = urlopen('http://fileserver:8983/solr/collection_name/select?q=cheese&wt=json')
response = simplejson.load(connection)
print response['response']['numFound'], "documents found."
 
# Print the name of each document.
 
for document in response['response']['docs']:
  print "  Name =", document['name']
