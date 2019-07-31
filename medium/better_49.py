class Solution:
	def groupAnagrams(self, strs):
	    d = {}
	    for w in sorted(strs):
	        key = tuple(sorted(w))
	        d[key] = d.get(key, []) + [w]	#get(key, default_value) default value is take place when no value in dict[key]
	    return d.values()