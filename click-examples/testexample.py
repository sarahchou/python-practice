# An example I found to test Click
def test_example():
    @click.command()
    @click.argument('name')
    def hello(name):
        click.echo('Hello %s!' % name)

    runner = CliRunner()
    result = runner.invoke(hello, ['Peter'])
    print(result.exit_code)
    assert result.exit_code == 0
    print(result.output)
    assert result.output == 'Hello Peter!\n'
