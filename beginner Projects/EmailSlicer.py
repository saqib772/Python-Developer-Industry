# To create an email slicer with Python, our task is to write a program that can retrieve the username and the domain name of the email.
# Like I Type james772@gmail.com Answer Will be < james772> Domain name will be gmail.com

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)
