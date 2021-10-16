import argparse
import terminaltables

arg_parser = argparse.ArgumentParser(description='CLI to explore the ascii table.')

arg_parser.add_argument('-c', '--char', type=str, help='The character to be displayed.')
arg_parser.add_argument('-i', '--index', type=str, help='The index in the ASCII-Table of the character to be displayed.')

args = arg_parser.parse_args()

if args.char:
    tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex'],
                [args.char, ord(args.char), hex(ord(args.char))]]
    table = terminaltables.AsciiTable(tabledata)
    print(table.table)
elif args.index:
    tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex'],
                [chr(int(args.index)), int(args.index), hex(int(args.index))]]
    table = terminaltables.AsciiTable(tabledata)
    print(table.table)
else:
    tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex']]
    for i in range(0, 127):
        tabledata.append([chr(i), i, hex(i)])
    table = terminaltables.AsciiTable(tabledata)
    print(table.table)