from math import floor

def default_gap(h):
	return int(h//2)

def knuth_gap(h):
	return int((3**h)/2)

def hibbard_gap(h):
	return int((2**h) -1)
	
def enhanced_gap(h):
	return int(floor((h*3)/4))
	
def shell_sort(arr, gap_function=default_gap):
    n = len(arr)
    gap = gap_function(n)
    contador = 0
    
    while gap > 0:
        y_index = gap
        while y_index < len(arr):
            y = arr[y_index]
            x_index = y_index - gap
            contador += 1
            while x_index >= 0 and y < arr[x_index]:
                contador += 1
                arr[x_index + gap] = arr[x_index]
                x_index = x_index - gap
            arr[x_index + gap] = y
            y_index = y_index + 1
        gap = gap_function(gap)
        
    return contador

def bubblesort(vetor):
	_length = len(vetor)
	contador = 0
	for i in range(0, _length):
		for j in range(i + 1, _length):
			contador += 1
			if (vetor[i] > vetor[j]):
				aux = vetor[i]
				vetor[i] = vetor[j]
				vetor[j] = aux
	return contador

def bubblesort2(vetor):
	troca = True
	_length = len(vetor)
	contador = 0

	while (troca):
		troca = False
		for i in range(0, _length - 1):
			contador += 1
			if vetor[i] > vetor[i + 1]:
				aux = vetor[i]
				vetor[i] = vetor[i + 1]
				vetor[i + 1] = aux
				troca = True
	return contador

def selectionsort(vetor):
	_length = len(vetor)
	contador = 0
	for i in range(0, _length - 1):
		_min = i
		for j in range(i + 1, _length):
			contador += 1
			if vetor[j] < vetor[_min]:
				_min = j
		if vetor[i] != vetor[_min]:
			aux = vetor[i]
			vetor[i] = vetor[_min]
			vetor[_min] = aux
	return contador
