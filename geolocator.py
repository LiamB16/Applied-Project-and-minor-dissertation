# State table.
table = {
    ('X', '_'): ['_', 'R', 'T'],
    ('X', '0'): ['0', 'R', 'X'],
    ('X', '1'): ['1', 'R', 'Y'],
    ('Y', '_'): ['_', 'R', 'F'],
    ('Y', '0'): ['0', 'R', 'Y'],
    ('Y', '1'): ['1', 'R', 'X'],
}

# Tape input.
tape = list('01110001')
# Position on tape.
pos = 0
i = 0
# Initial state is first in table.
state = 'X'

# Keep going while we are not in a halting state.
while state not in ['T', 'F']:
    # Print the current status.
    print(''.join(tape[:pos]) + state + ''.join(tape[pos:]))
    # Get the row of the table.
    row = table[(state, tape[pos])]
    # Overwrite the symbol.
    tape[pos] = row[0]
    for i in range(len(tape)):
       if tape[i] != 1:
    # Move left or right.
        if row[1] == 'R':
        # Put blanks on tape as necessary.
            if pos == len(tape) - 1:
               tape = tape + ['_']
        # Increase position.
            pos = pos + 1
        else:
        # Put blanks on tape as necessary.
            if pos == 0:
               tape = ['_'] + tape
            # The position on the tape has to move with it.
               pos = pos + 1
        # Increase position.
            pos = pos - 1
    # Update the state.
        state = row[2]

# Print the current status.
print(''.join(tape[:pos]) + state + ''.join(tape[pos:]))