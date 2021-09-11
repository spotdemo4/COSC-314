import argparse
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(description="Finds the truth values of the conjunction, disjunction, exclusive or, conditional statement, and biconditional of the given propositions.")
    parser.add_argument('prop1', metavar="Prop1", type=str.upper, help="First proposition (T/F)")
    parser.add_argument('prop2', metavar="Prop2", type=str.upper, help="Second proposition (T/F)")
    return parser.parse_args(args)

#Conjunction
def getAnd(p1, p2):
    return p1 == "T" and p2 == "T"

#Disjunction
def getOr(p1, p2):
    return p1 == "T" or p2 == "T"

#Exclusive or
def getXor(p1, p2):
    return p1 != p2

#Conditional statement
def getImplies(p1, p2):
    return p1 != "T" or p2 == "T"

#Biconditional statement
def getIff(p1, p2):
    return p1 == p2

if __name__ == "__main__":
    parser = parse_args(sys.argv[1:])

    if parser.prop1 not in {"T", "F"}:
        raise ValueError("Proposition 1 needs to be T or F, not '" + parser.prop1 + "'")

    if parser.prop2 not in {"T", "F"}:
        raise ValueError("Proposition 2 needs to be T or F, not '" + parser.prop2 + "'")

    print("Conjunction: " + str(getAnd(parser.prop1, parser.prop2)))
    print("Disjunction: " + str(getOr(parser.prop1, parser.prop2)))
    print("Exclusive Or: " + str(getXor(parser.prop1, parser.prop2)))
    print("Conditional: " + str(getImplies(parser.prop1, parser.prop2)))
    print("Biconditional: " + str(getIff(parser.prop1, parser.prop2)))