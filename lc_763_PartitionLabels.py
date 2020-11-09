class Solution(object):
    def partitionLabels(self, S):
        """
        put the smae char stay in same slot
        "ababcbacadefegdehijhklij"
        
        as long as cur appeared in the previous state, than combine
            {char1:g_id}
           {g_id  : [char1, char2, c3,..]}
           if cur exist: combine every g_id which less than cur_gid and larger than 
           update g_id and it contant and effected char/ it's grops
           ababcbacadefegdehijhklij
           ababcbaca defegde hijklij 
        """

        char_id = {} #{char1:g_id}
        glst = {} #{g_id  : [char1, char2, c3,..]}
        gid  = 0
        for idx, v in enumerate(S):
            """
            char_id = {"a": 1, "b":1, }
            glst = {1: [a,b,a]}
            """
            if v in char_id:
                s_id = char_id[v]
                e_id = gid
                
                for up_id in range(s_id + 1, e_id+1): 
                    if up_id not in glst:
                        continue
                    for e in glst[up_id]:
                        char_id[e] = s_id #update the gid of a char    
                    glst[s_id] += glst[up_id] #combine groups
                    del glst[up_id] #remvo empty group
                glst[s_id].append(v)
            else:
                gid += 1 
                char_id[v] = gid
                glst[gid] = [v]
        return [len(v) for e, v in glst.items()]
