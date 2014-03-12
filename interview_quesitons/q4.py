'''
Given a table:

Name    Size   Color    ...
AAA     Med    Red      ...
BBB     Med    Red      ...
CCC     Big    Blue     ...
DDD     Big    Red      ...
EEE     Small  Blue     ...

Input:   String[][] table, and String[] order = {"Color", "Size", "Name"...}
Output:
Red
    Med
         AAA
         BBB
    Big
         DDD
Blue
    Small
         EEE
    Big
         CCC

Note "order" gives the order of the output of the columns.
'''
from operator import itemgetter

# def print_sorted(sorted_table):
    # for row in sorted_table:

def reset(sorted_table, index_mapping):
    rt = []
    for row in sorted_table:
        n_row = [None] * len(row)
        for i in xrange(len(row)):
            n_row[index_mapping[i]] = row[i]
        rt.append(n_row)
    return rt

def print_level(reset_table):
    for row_num in xrange(len(reset_table)):
        row = reset_table[row_num]
        for col_num in xrange(len(row)):
            item = row[col_num]
            if row_num == 0 or item != reset_table[row_num - 1][col_num]:
                print('{}{}'.format('\t'*col_num, row[col_num]))

def foo(table, order):
    '''
    Args:
        table: list of list. Example: [['Name', 'Size', 'Color'], ['AAA', 'Med', 'Red'], ['BBB', 'Med', 'Red']]
        order: list. Example: ['Color', 'Size', 'Name']
    '''
    titles = table[0]
    index_mapping = [order.index(name) for name in titles]
    sorted_table = sorted(table[1:], key=itemgetter(*index_mapping))
    reset_table = reset(sorted_table, index_mapping)
    print_level(reset_table)

table = [['Name', 'Size', 'Color'], 
    ['AAA', 'Med', 'Red'], 
    ['BBB', 'Med', 'Red'],
    ['CCC', 'Big', 'Blue'],
    ['DDD', 'Big', 'Red'],
    ['EEE', 'Small', 'Blue']]
order = ['Color', 'Size', 'Name']

print foo(table, order)
