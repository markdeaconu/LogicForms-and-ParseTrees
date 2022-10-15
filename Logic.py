from config import *
from lib204 import semantic_interface

# statement 1 is (~((T&Q)|R)>>(~T|~R))

# statement 2 is (~(T|~R)|(~R>>(Q&~T)))

statement1nnf = [
    [(~((T&Q)|R)>>(~T|~R)), 'starting formula'],
    [((~(T&Q)&~R)>>(~T|~R)), 'demorgans law'],
    [(((~T|~Q)&~R)>>(~T|~R)), 'demorgans law'],
    [~((~T|~Q)&~R)|(~T|~R), 'Turning implication to disjunction'],
    [(~(~T|~Q)|R)|(~T|~R), 'demorgans law'],
    [((T&Q)|R)|(~T|~R), 'demorgans law and double negation']
]

statement2nnf = [
    [(~(T|~R)|(~R>>(Q&~T))), 'starting formula'],
    [((~T&R)|(~R>>(Q&~T))), 'demorgans law'],
    [((~T&R)|(R|(Q&~T))), 'turning implication to disjunction and double negation']
]

statement1cnf = [
    [(~((T&Q)|R)>>(~T|~R)), 'starting formula'],
    [((~(T&Q)&~R)>>(~T|~R)), 'demorgans law'],
    [(((~T|~Q)&~R)>>(~T|~R)), 'demorgans law'],
    [~((~T|~Q)&~R)|(~T|~R), 'Turning implication to disjunction'],
    [(~(~T|~Q)|R)|(~T|~R), 'demorgans law'],
    [((T&Q)|R)|(~T|~R), 'demorgans law and double negation'],
    [((T|R)&(Q|R))|(~T|~R), 'distrubution'],
    [(((T|R)|(~T|~R))&((Q|R)|(~T|~R))), 'distrubution']
]

statement2cnf = [
    [(~(T|~R)|(~R>>(Q&~T))), 'starting formula'],
    [((~T&R)|(~R>>(Q&~T))), 'demorgans law'],
    [((~T&R)|(R|(Q&~T))), 'turning implication to disjunction and double negation']
    [((~T&R)|((R|Q)&(R|~T))), 'distribution']
    [((~T&R)|(R|Q)) & ((~T&R)|(R|~T)), 'distribution']

]

statement1tseitin = semantic_interface.Encoding()
x1 = statement1tseitin.tseitin(T & Q, 'x1')
x2 = statement1tseitin.tseitin(x1 | R, 'x2')
x3 = statement1tseitin.tseitin(~x2 , 'x3')
x4 = statement1tseitin.tseitin(~T, 'x4')
x5 = statement1tseitin.tseitin(~Q, 'x5')
x6 = statement1tseitin.tseitin(x4 | x5, 'x6')
x7 = statement1tseitin.tseitin(x6 >> x3, 'x7')

statement1tseitin.finalize(x7) 

statement2tseitin = semantic_interface.Encoding()
x1 = statement2tseitin.tseitin(~R, 'x1')
x2 = statement2tseitin.tseitin(T & x1, 'x2')
x3 = statement2tseitin.tseitin(~x2, 'x3')
x4 = statement2tseitin.tseitin(~T, 'x4')
x5 = statement2tseitin.tseitin(Q & x4, 'x5')
x6 = statement2tseitin.tseitin(~R, 'x6')
x7 = statement2tseitin.tseitin(x6 >> x5, 'x7')
x8 = statement2tseitin.tseitin(x3 | x7, 'x8')
statement2tseitin.finalize(x8) 
