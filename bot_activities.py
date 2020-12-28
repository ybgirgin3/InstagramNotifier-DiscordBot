act = ['Drifting', 'Driving', 'Trying to reach top speed of']
car = ['M2','M4', 'M3', 'M5', '730Li', 'M6']
at = ['Forza Horizon 4', 'Neighbours garden', 'Highway', 'In the Sea']


import random

def stat():
    activity = '{0} a {1} in the {2}'.format(
            random.choice(act),
            random.choice(car),
            random.choice(at)
            )
    return activity


