import click
@click.command()
#@click.option('--type', type=click.Choice(['Terraform', 'Ansible', 'terr']), help="Choose either Terraform or Ansible")
@click.option('--type', prompt='What kind of code are you generating?', help='Choose Terraform or Ansible.')
@click.option('--url', prompt='What is the URL to the Terraform DSL file?', help='Specify file path.')

def terraform_or_ansible(type,url):

	if (type == 'Terraform' or type == 'Ansible'):
		click.echo("You chose %s." % type)
	else:
		print("Input not supported. Please try again, and indicate Terraform or Ansible.")
	click.echo("The URL is {0}".format(url))

if __name__ == "__main__":
    terraform_or_ansible()
