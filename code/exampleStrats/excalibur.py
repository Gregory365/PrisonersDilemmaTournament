import numpy as np

def strategy(history, memory):
    """
    Aims to calculate chance of opponent defecting based on our own decision
    Attempts to chose the option that maximises the number of points
    """
    choice = 1
    if history.shape[1] > 0:
        # start with titForTat to try and deceive detectives
        if history.shape[1] <= 6:
            choice = history[1,-1]

        else:
            # shift history to allign actions with consectutive response
            us = history[0][:-1]
            them = history[1][1:]
            length = len(them)
            lastTurn = int(history[0, -1])

            # points - meaning
            # [1, 5]   [we defect and they defect,    we defect and they cooperate]
            # [0, 3]   [we cooperate and they defect, we cooperate and they cooperate]
            results = np.array([[0, 0], [0, 0]])
            for i in range(length):
                results[us[i], them[i]] += 1
            
            ourTotalDefections = int(results[0, 0] + results[0, 1])
            ourTotalCooperations = int(results[1, 0] + results[1, 1])
            TheyCoorporateWhenWeDont = results[0, 1] / (ourTotalDefections + 1)
            TheyCoorporateWhenWeDo = results[1, 1] / (ourTotalCooperations + 1)

            # exploit (defect), if the coorporate frequently when we defect
            if TheyCoorporateWhenWeDont > 2/3:
                choice = 0
            # defect, if we need more data on how they react to defections
            elif 2**(ourTotalDefections - lastTurn + 1) < (length + 1):
                choice = 0
            # cooporate, if we need more data on how the react to cooporations
            elif 2**(ourTotalCooperations + lastTurn) < (length + 1):
                choice = 1
            # defect, if they are more likely to coorporate when we defect
            elif TheyCoorporateWhenWeDont > TheyCoorporateWhenWeDo:
                choice = 0

            # use tikForTat if they defect infrequently and we can't exploit them
            else:
                # don't use titForTat if we defected 2 turns ago (as they could be paying revenge)
                # and  would rather both coorporate together than defect together
                if history[0, -2]:
                    choice = history[1,-1] #titForTat
                else:
                    # if all else fails, providing they are cooporating most the time, we should cooporate too
                    choice = TheyCoorporateWhenWeDo > 2/3

    return choice, None