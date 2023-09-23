def twoSum( numbers, target):
        indices = []

        for n_i, n in enumerate(numbers):
            for n_j, j in enumerate(numbers[n_i+1:]):
                if n + j == target:
                    print(n)
                    print(j)
                    print(n_i)
                    print(n_j)
                    indices = [n_i+1, n_j+2] 

        return indices

numbers =[5,25,75]
target = 100

twoSum(numbers,target)