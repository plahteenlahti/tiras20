def count(s):
    count = [0]*3
    history = {}
    history[(0,0)] = 1
    result = 0
    for c in s:
        count[ord(c)-65] += 1
        diffs = (count[0]-count[1],count[0]-count[2])
        result += history.get(diffs,0)
        history[diffs] = history.get(diffs,0)+1
    return result


if __name__ == "__main__":
	print(count("CCAABB")) # 1
	print(count("CBACBA"),count("CBACBA") == 5) # 5
	print(count("AAABBC")) # 0
	print(count("CCBCCCABB")) # 1