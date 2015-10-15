#!/usr/bin/python
# Grant David Meadors
# 02015-10-15 (JD 2457311)
# g r a n t . m e a d o r s @ a e i . m p g . d e
# Experiment to learn how to manipulate frames in SQL using Python,
# later to be adapted to R

import sqlite3

conn = sqlite3.connect('exampleTSoutput.db')
# Create a connection
c = conn.cursor()

# Format the database
c.execute('''CREATE TABLE twospectout
             (fsig real, period real, df real, ra real, dec real, r real, h0 real, prob real, tfnorm real)''')

# Specify example values
templates = [
            (74.043000, 68023.825900, 0.0133342, 4.2757, -0.2730, 93.9088, 1.10763e-24, -4.8475, 3.49802e+45),
            (74.043000, 68023.825900, 0.0136296, 4.2757, -0.2730, 94.3590, 1.10895e-24, -4.5989, 3.49802e+45),
            (74.043000, 68023.825900, 0.0139251, 4.2757, -0.2730, 101.6311, 1.12973e-24, -4.8166, 3.49802e+45)
             ]
# Actually insert values into table
c.executemany('INSERT INTO twospectout VALUES (?,?,?,?,?,?,?,?,?)', templates)

# Print the values
for row in c.execute('SELECT * FROM twospectout ORDER BY fsig'):
    print row

# Close connection
conn.close()

# NEXT, see if we can import an R data frame
#from rpy2.robjects import pandas2ri
