def query(q,filename):

  sparql.setQuery(q)
  sparql.setReturnFormat(JSON)
  ret = sparql.query()

  results = ret.convert()
  results_df = pd.io.json.json_normalize(results['results']['bindings'])

  if results_df.empty == False:
  results_df[['item.value', 'itemLabel.value','itemDescription.value']].head()

  df = results_df[['item.value', 'itemLabel.value','itemDescription.value']]
  print(df.head)
  df.to_csv(filename,index=False)

  return df
  else:
  print("\tNo related information!")

  return "None"

def checkOcupation(QID):
  res = """
  SELECT ?item ?itemLabel ?itemDescription
  WHERE
  { wd:"""+QID+""" wdt:P106 ?item
  SERVICE wikibase:label
  { bd:serviceParam
  wikibase:language "en"
  }
  } LIMIT 100

  """

  query(res)
  return res