def anagrams(words):
    ans={}

    for eachWord in words:
        sorted_word=''.join(sorted(eachWord))
        if sorted_word in ans:
            ans[sorted_word].append(eachWord)
        else:
            ans[sorted_word]=[eachWord]
    return list(ans.values())

words=['eat','tea','tan','ate','nat','bat']
print(anagrams(words))
