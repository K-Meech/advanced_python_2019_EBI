
import numpy as np

def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    list_of_maxima = []
    for i, intensity in enumerate(list_of_intensities):
        if i == 0 or i == len(list_of_intensities) - 1:
            continue
        if list_of_intensities[i - 1] < intensity and list_of_intensities[i + 1] < intensity:
            list_of_maxima.append(intensity)
    return list_of_maxima
