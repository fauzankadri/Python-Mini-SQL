# Functions for reading tables and databases


import glob

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

file_list =  glob.glob('*.csv')


# Write the read_table and read_database functions below

#reads a single file and generates a table of that file
def read_table(file):
    '''
    (str) -> table
    
    >>> res = read_table('movies.csv')
    >>> output = {'m.studio': ['Par.', 'NL', 'BV'], \
        'm.gross': ['2186.8', '1119.9', '1063.2'], \
        'm.title': ['Titanic', \
        'The Lord of the Rings: The Return of the King', 'Toy Story 3'], \
        'm.year': ['1997', '2003', '2010']}
    >>> res == output
    True
    
    
    Returns a dict of tables
    '''
    table_list = []
    opened_file = open(file, 'r')
    #reads each line in file and adds to a list
    for line in opened_file:
        if line[-1] == '\n':
            line = line[:-1]  # removes \n
        line = line.split(',')
        #adds line to a list
        table_list.append(line)
    opened_file.close()
    #deletes any empty list
    while [''] in table_list:
        table_list.remove([''])
    table_dict = {}
    temp_list = []
    #creates a list for each key to add to
    for i in range(0, len(table_list[0])):
        for j in range(1, len(table_list)):
            #gets the appropriate values for the given key
            temp_list.append(table_list[j][i])
        table_dict[table_list[0][i]] = temp_list
        #resets the temp_list
        temp_list = []
    return table_dict


#reads all files and stores them as a table of dict using read_table(file)
def read_database():
    '''
    None -> database
    
    >>> res = read_database()
    >>> output = {'movies': {'m.year': ['1997', '2003', '2010'], \
        'm.gross': ['2186.8', '1119.9', '1063.2'], \
        'm.studio': ['Par.', 'NL', 'BV'], \
        'm.title': ['Titanic', \
        'The Lord of the Rings: The Return of the King', 'Toy Story 3']}, \
        'oscars': {'o.title': ['Toy Story 3', \
        'The Lord of the Rings: The Return of the King', \
        'Titanic', 'Titanic'], \
        'o.category': ['Animated Feature Film', \
        'Directing', 'Directing', 'Best Picture'], \
        'o.year': ['2010', '2003', '1997', '1997']}}
    >>> res == output
    True
    
    
    Returns the dictionary of all files in glob inside a dictionary
    '''
    database_dict = {}
    #reads each file indivdually
    for file in file_list:
        #stores the dictionary of the specific file
        res = read_table(file)
        #creates a key of the file name
        key = file[:-4]
        #stores a new dictionary of the key and dictionary
        database_dict[key] = res
    return database_dict