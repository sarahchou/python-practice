from argparse_prompt import PromptParser

parser = PromptParser()
parser.add_argument('--argument', '-a', help='Choose either Ansible or Terraform', default='Ansible or Terraform?')
parser.add_argument('--filepath', '-fp', help='Specify file path', default='Whats the file path?')

argument = parser.parse_args().argument
filepath = parser.parse_args().filepath
if (argument == 'Terraform' or argument == 'Ansible'):
	print("You chose: " + argument)
else: 
	print("Incorrect input. Must choose either Ansible or Terraform. Please try again.")
print("Selected file path is: " + filepath)
