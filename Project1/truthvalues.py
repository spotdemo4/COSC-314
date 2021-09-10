import argparse
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(description="Finds the truth values of the conjunction, disjunction, exclusive or, conditional statement, and biconditional of the given propositions.")
    parser.add_argument('prop1', metavar="Prop1", type=str.upper, help="First proposition (T/F)")
    parser.add_argument('prop2', metavar="Prop2", type=str.upper, help="Second proposition (T/F)")
    return parser.parse_args(args)

#Conjunction
def getAnd(p1, p2):
    if p1 == "T" and p1 == p2:
        return True
    else:
        return False

#Disjunction
def getOr(p1, p2):
    if p1 == "T" or p2 == "T":
        return True
    else:
        return False

#Exclusive or
def getXor(p1, p2):
    if p1 != p2:
        return True
    else:
        return False

#Conditional statement
def getImplies(p1, p2):
    if p1 == "T" and p2 == "F":
        return False
    else:
        return True

#Biconditional statement
def getIff(p1, p2):
    if p1 == p2:
        return True
    else:
        return False

if __name__ == "__main__":
    parser = parse_args(sys.argv[1:])

    if parser.prop1 not in {"T", "F"}:
        print("Proposition 1 needs to be T or F, not " + parser.prop1)
        exit()

    if parser.prop2 not in {"T", "F"}:
        print("Proposition 2 needs to be T or F, not " + parser.prop2)
        exit()

    print("Conjunction: " + str(getAnd(parser.prop1, parser.prop2)))
    print("Disjunction: " + str(getOr(parser.prop1, parser.prop2)))
    print("Exclusive Or: " + str(getXor(parser.prop1, parser.prop2)))
    print("Conditional: " + str(getImplies(parser.prop1, parser.prop2)))
    print("Biconditional: " + str(getIff(parser.prop1, parser.prop2)))