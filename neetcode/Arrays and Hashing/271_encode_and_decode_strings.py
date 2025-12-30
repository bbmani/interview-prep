class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Final Result
        res = ""

        for word in strs:
            # Storing the length of the word followed by any delimiter.
            res += str(len(word)) + "$" + word
        
        # Returning the result. 
        return res
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # Return value is going to be an array
        res = []

        # Starting index
        idx = 0

        # Iterate through the entire string
        while idx < len(s):
            jdx = idx

            # Iterate through until you hit the demiliter
            while s[jdx] != "$":
                jdx += 1
            
            # The length is going to be from idx to jdx (not inclusive)
            length = int(s[idx:jdx])

            # The word is going to be from jdx + 1 until jdx + 1 + length
            res.append(s[jdx + 1 : jdx + 1 + length])

            # Look for the next word after jdx + 1 + length
            idx = jdx + 1 + length

        return res

         
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
