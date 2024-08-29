''' ITERATION 3

Module: Suarez Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this third iteration, I declare additional variables to show skills with different data types.'''

#####################################
# Declare a global variables - keep byline at the end
#we will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

#Integer variable for the number of years in operation
years_in_operation: int = 10

#List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

#List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Declare a global variable named byline.
#Make it a multiple f-string to show our information
#####################################

byline: str = f"""
------------------------------------------------------
Suarez Analytics: Delivering Solutions and Insights
------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operations:        {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction scores: {client_satisfaction_scores}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline
    
#####################################
# Define a main() function for this module.
#####################################

#The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
    
