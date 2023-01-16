import time

intro = "Hi! You will help the little boy businessman Mark Zuckerman to find out if his new project will be successful."
idea = "A young computer genius named Mark Zuckerman started thinking about an idea for creating a famous website."
is_able = "Do you think Mark has all what it takes?"
not_able = "Having burned through 20-billion-dollar for his crapshoot project, Mark decided to open a really cool animal shelter project and called it MuzzleBook."
go_ahead = "Mark Zuckerman asked his school friend Elon Must advise if to roll the dice investing in social network and Elon said: no way."
asking_Elon = "Should Mark go ahead for social media business if Elon said no way?"
go_ahead_again = "Mark does not listen to Elon's warning. And started work on his social media project."
meta_project = "After having lost investors Mark decided to change project name and calls it Meta-worse."
to_continue = "Will he have success?"
meta_worse_continue = "Thanks for helping Mark out! After another billion spent, Mark receives a message from Elon asking if Mark wants to buy from him network called Titter"
titter = 'Mark purchases Titter. He makes it!'
try_again = "Should he try get more networks?"
hookup_gram = "Mark gets new network HookUpGram: HUG"
hookup_gram_details = "As it is only used by people for dating - business does not bring revenue"
quit_hookup_gram = "Does Mark have to close HookUpGram?"
yes_quit_hookup_gram = "Mark closes business."
no_quit_hookup_gram = "Mark stays there for good but investors run to new successfull business - Roma - a really cool inventor"
   
def yes_or_no():
    condition_to_run = False
    while condition_to_run == False:
        output=input("Say yes or no: ")
        if (output == 'Yes') or (output == 'yes'):
            return(True)
            condition_to_run = True
        elif (output == 'No') or (output == 'no'):
                return(False)
                condition_to_run = True
        else:
                print("Please write more clear yes or no.")

def project_prospects():
    keep_running = False
    print("Mark needs to choose a project to work on. What to choose: Meta, Titter or Hug (HookUpGram).")
    while keep_running == False:
        decision = input("Which one is more promising?")
        if (decision == "Meta") or (decision == 'meta'):
            keep_running = True
            print(meta_project)
            print(to_continue)
            if yes_or_no():
                print(meta_worse_continue)
            else:
                print(not_able)
        elif (decision == 'Titter') or (decision == 'titter'):
            print(titter)
            keep_running = True
        elif (decision == 'Hug') or (decision == 'hug'):
            keep_running = True
            print(hookup_gram)
            print(hookup_gram_details)
            print(quit_hookup_gram)
            if yes_or_no():
                print(yes_quit_hookup_gram)
                print(try_again)
                if yes_or_no():
                    print("Mark tries again. Although he has to lay off all employees")
                    keep_running = False
                else:
                    print(not_able)
            else:
                print(no_quit_hookup_gram)
        else:
            print("This option does not excist. Please try again.")
        
        

def mark_business():
    print(intro)
    time.sleep(2)
    print(idea)
    time.sleep(3)
    print(is_able)
    if not yes_or_no():
        print(not_able)
    else:
        print(go_ahead)
        print(asking_Elon)
        if not yes_or_no():
            print(not_able)
        else:
            print(go_ahead_again)
            project_prospects()
    time.sleep(3)

mark_business()
        
            
    
        
    
