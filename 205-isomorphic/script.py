def isIsomorphic(s, t):
    ## if strings are not same length, they're not isomorphic
    if len(s) != len(t):
        return False
    
    ## create dictionaries to store the mappings
    s_dict = {}
    t_dict = {}

    ## iterate through the strings
    for i in range(len(s)):
        ## if the mappings are different, return False
        if s_dict.get(s[i]) != t_dict.get(t[i]):
            return False
        ## if the mappings are not in the dictionary, add them
        s_dict[s[i]] = i
        t_dict[t[i]] = i
    return True

