import click

@click.command()
@click.option('--color', prompt='What color?', help='Pick a color.')
def main(color):
    click.echo('color=%s' % color)


if __name__ == "__main__":
    main()

