from cmd import PROMPT


def monthly():
    """"Listing MTN monthly data plan"""
    plan = ['Back','N1000 for 1.5GB','N1200 for 2GB', 'N1500 for 3GB', 'N2000 for 4.5GB',
            'N2500 for 6GB', 'N3500 for 12GB', 'N1000 for 1.5GB+N1000', 'N5000 for 20GB', 'N10000 for 40GB',
            'N15000 for 75GB', 'N20000 for 120GB', 'N30000 for 200GB', 'N000 for 4.5GB+N2000 Talktime']
    
    num = 0
    for p in plan:
        print(f'{num},{p}')
        num += 1
    lent = len(plan)
    return lent

#monthly()

def weekly():
    """"Listing MTN monthly data plan"""
    plan = ['Back','N200 for 1GB(IG&TIKTOK ONLY)','N300 for 350MB', 'N500 for 750MB(2-Week Plan)', 
            'N500 for 750MB+N500 Talktime (Val/14days)','N1500 for 6GB', 'N1000 for 2GB', 
            'N500 for 1GB', 'N50 for whatsapp weekly', 'N500 for 750MB (Youtube Bundle)']
    
    num = 0
    for p in plan:
        print(f'{num},{p}')
        num += 1
    lent = len(plan)
    return lent

#weekly

def choice():
    prompt = '1. Weekly plan'
    prompt += '\n2. Monthly Plan'
    print(prompt)
    try:
        user = int(input('_ '))
        print('\n')
        return user
    except ValueError:
        print('Response Timeout.')
        
#me = choice()

def bundle():
    """Works with client's bundle decision"""
    prompt = 'Do you want to bundle?'
    prompt += '\nPress enter otherwise type no _'
    user = input(prompt)
    if user == '':
        print('You have bundled successfully')
    else:
        print('Invalid response, try again.')