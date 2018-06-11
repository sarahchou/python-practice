import click
@click.command()
@click.option('--type', prompt='What kind of code are you generating?', help='Indicate Terraform or Ansible.')
@click.option('--url', prompt='What is the URL to the Terraform DSL file?', help='Specify file path.')

def generation_type(type,url):

	if (type == 'Terraform' or type == 'Ansible'):
		click.echo("You chose %s." % type)
		click.echo("The file path is {0}".format(url))
	else:
		print("Input not supported. Please try again, and indicate Terraform or Ansible.")
	

if __name__ == "__main__":
    generation_type()
