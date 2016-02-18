from Pyglish import Synonyms

syn = Synonyms()

#  Get all relevant
print "SURE: %s" % str(syn.get_all("sure"))
print "ROAD: %s" % str(syn.get_all("road"))

#  Get the best
print "ALL RIGHT: " + syn.get_best("all right")
print "GRITTY: " + syn.get_best("gritty")
