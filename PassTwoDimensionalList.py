'''
        From P366 Chapter 11 Multidimensional Lists
'''

def getMatrix():
    matrix = []

    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(numberOfColumns):
        # Add an empty new row
        matrix.append([])
        for column in range(numberOfColumns):
            value = eval(input("Enter a value and press Enter: "))
            matrix[row].append(value)

    return matrix
def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)
    return total

def main():
    m = getMatrix()
    print(m)

    print("\nSum of all elements is", accumulate(m))

main()
