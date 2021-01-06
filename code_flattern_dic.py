"""
loop k,v as dic.items() recurively, when v is not str
terminate rule: obj's type is str
"""

d = {
    "Key1" : "1",
    "Key2" : {
        "a" : "2",
        "b" : "3",
        "c" : {
            "d" : "3",
            "e" : "1"
        }
    }
}

def flattern_dic(dic):
	res = {}
	def dfs(obj,key):
		if isinstance(obj, str):
			res[key[1:]] = obj
			return 
		
		for k, value in obj.items():
			dfs(value, key +"."+ k)
	dfs(dic,"")
	return res
