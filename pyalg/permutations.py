
def generate_permutations(n: int) -> List[List[int]]:
	assert n > 0
	
	if n == 1:
		return [[1]]
	else:
		return [L[:i] + [n] + L[i:] for L in generate_permutations(n - 1) for i in range(n)]