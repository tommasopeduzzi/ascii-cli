import argparse
import terminaltables
import click

@click.command()
@click.option('--char', default=None, help='Character to be displayed')
@click.option('--index', default=None, help='Character to be displayed')


def asciicli(char, index):
    if char:
        tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex'],
                    [char, ord(char), hex(ord(char))]]
        table = terminaltables.AsciiTable(tabledata)
        print(table.table)
    elif index:
        tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex'],
                    [chr(int(index)), int(index), hex(int(index))]]
        table = terminaltables.AsciiTable(tabledata)
        print(table.table)
    else:
        tabledata = [['Character', 'ASCII Code', 'ASCII Code Hex']]
        for i in range(0, 127):
            tabledata.append([chr(i), i, hex(i)])
        table = terminaltables.AsciiTable(tabledata)
        print(table.table)

if __name__ == '__main__':
    asciicli()