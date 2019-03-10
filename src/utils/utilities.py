# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    
    Args:
        iteration  (int): Required  : current iteration (Int)
        total      (str): Required  : total iterations (Int)
        prefix     (str): Optional  : prefix string (Str)
        suffix     (str): Optional  : suffix string (Str)
        decimals   (int): Optional  : positive number of decimals in percent complete (Int)
        length     (int): Optional  : character length of bar (Int)
        fill       (str): Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
