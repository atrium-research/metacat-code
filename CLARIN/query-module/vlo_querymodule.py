import json
import jsonpath
import requests

def extractFacetValues(collectionJson):
    facets = json.loads(collectionJson)
    print(f'Processing query collection definition containing {len(facets)} facets.')
    
    result = {}
    for facet in facets:
        if facet['catalogue'] == 'vlo' and facet['url']:
            name = facet['facet']
            url = facet['url'];
            print (f'* Retrieving data for facet \'{name}\' at <{url}>')
            
            # Get facet values and counts
            responseJson = requests.get(url).json()
            facetValues = jsonpath.findall('$.values[*].value', responseJson)
            facetCounts = jsonpath.findall('$.values[*].count', responseJson)
            result[name] = dict(zip(facetValues, facetCounts));        

    return result