import click
from click.testing import CliRunner

def test_colors_prompts():
    @click.command()
    @click.option('--color', prompt='What color?', help='Pick a color.')
    def main(color):
        click.echo('color=%s' % color)

    runner = CliRunner()
    result = runner.invoke(main, input='orange\n')
    assert not result.exception
    print("new line")
    print(result.output)
    assert result.output == 'What color?: orange\ncolor=orange\n'



if __name__ == "__main__":
    test_colors_prompts()

