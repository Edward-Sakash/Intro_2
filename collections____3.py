A = ['x', 'y', 'z']
B = [1, 2, 3]

def cartesian_prod(A,B):
    result = []
    for itemA in A:
        for itemB in B:
            result.append((itemA, itemB))
    return result
        
result = cartesian_prod(A,B)
print(result)

print('________________________________')

board = [['_'] * 3 for num in range(3)] # working
board[1][2] = 'X'
weird_board = [['_'] * 3] * 3
weird_board[1][2] = 'O' # weird behavior

one_line = ['_'] * 3
two_line = one_line
three_line = one_line
weird_board2 = [one_line, two_line, three_line]

one_line = ['_'] * 3
two_line = one_line[:]
three_line = one_line[:]
weird_board2 = [one_line, two_line, three_line]
weird_board2[0][0] = '0'
weird_board

print('________________________________')

books = [('hello', 3), ('world', 1), ('again', 2)]

def sort_helper(item):
    return item[1]

print(sorted(books, key=sort_helper))
#print(sorted(books))

number = [[1,2], [1,1], [0,1]]
print(sorted(number, key=sum))

print(books[0][0])


