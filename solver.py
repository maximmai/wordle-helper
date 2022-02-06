class Solver(object):

    def __init__(self, k=5):
        self.current_scope = []
        self.result = []
        self.k = k

    """
    result_state: [
        {
            key: char,
            value: int, -1 wrong character, 0 right character but wrong position, 1 right character and right position
        }
    ]
    """
    def parse_result(self, state):
        for i in range(self.k):
            # character has been identified, skip
            if self.current_scope[i]["final"] != "":
                continue

            key, value = state[i]
            
            # -1 wrong character, should remove occurrances in all position scope sets
            if value == -1:
                self.current_scope[i]["chars"].discard(key)
            
            # 0 right character but wrong position, should remove from the ith position of scope set, and should fav in other non final sets
            elif value == 0:
                self.current_scope[i]["chars"].discard(key)
                self.current_scope[i]["whitelist"].discard(key)
                self.current_scope[i]["blacklist"].add(key)

                for j in range(self.k):
                    if j != i and self.current_scope[j]["final"] == "" and key not in self.current_scope[j]["blacklist"]:
                        self.current_scope[j]["whitelist"].add(key)
                
                
            # 1 right character and right position, update the scope set to just the character
            elif value == 1:
                self.current_scope[i]["final"] = key
    
    """
    should search the prefix tree for the best next character in fav
    """
    def find_in_dictionary(self, prefix, fav):
        pass

    """
    scope is a simple struct: 
    {
        chars: set()
        fav: set()
    }
    """
    def get_next_word(self):
        result = [""] * self.k
        for i in range(self.k):
            chars, fav = self.current_scope[i]
            if len(fav) > 0:
                # should pick one from this
                result[i] = self.find_in_dictionary(result[:i], fav)
            else:
                # pick one from chars
                result[i] = self.find_in_dictionary(result[:i], chars)

        result = "".join(result)
        return result