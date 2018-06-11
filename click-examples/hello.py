import click

@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.option('--sarah', default='', help='Trying my own.')
#@click.password_option()
@click.argument('country')
def cli(verbose,name,sarah,country): #add in password
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    if sarah: 
    	click.echo('A secret message. Hi {0}'.format(sarah))
    click.echo("Hello {0}".format(country))
    #click.echo("Hello World")
    for n in name: 
    	click.echo('Bye {0}'.format(n))
    if sarah:
    	click.echo('P.S. {0}'.format(sarah) + ' says hi')
    #click.echo('We received {0} as password.'.format(password)) #NEVER PRINT PASSWORDS this is just an example
