class Sol:
    def reverse_words_in_a_string(self,s):
        arr1=s.split()
        l=len(arr1)
        for x in range(l):
            arr1.append(arr1[x][::-1])
        return arr1[l:]
