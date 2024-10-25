import googlesearch  # for accessing Google search

query = "University of Greenwich"
""" get the first 5 results, 1 at a time, pausing 2 seconds between each
    if the pause value is too small, Google may block the search """
for search_result in googlesearch.search(query, stop=5, num=1, pause=2):
    print(search_result)
