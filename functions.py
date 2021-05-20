#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:
#   - Erik Zaborowski
#   - Finian Ashmead
#   - Isaac Sierra
#   - Mike Gladders

import os
import numpy as np
from astropy.io import fits

def process_single_file(input_file):
    """
    Function to take a FITS image and subtract the mean value of the
    overscan area of the CCD.

    :param input_file:    (str) filepath of the image to process
    :returns output_hdul: (astropy.io.fits.HDUList) processed version of the fits file
    """
    # TODO: Add code below...

    return output_hdul


def process_single_object(control_file, input_dir, output_dir):
    """
    Function to loop through the files in the input directory and process/rename/save
    them in the format expected by the IRAF code.
    
    Control file should be in the format (one object per line):
        science1 science2 flat1 flat2 arc1 arc2 ... arcN
        science1 science2 flat1 flat2 arc1 arc2 ... arcN
        ...
    But filled in with the filenames of the images to process.
    
    Perhaps within the output directory, should create a subdirectory for each
    object, which contains the processed sci1.fits, sci2.fits, etc for that object.

    :param control_file: (str) path to file specifying the available images
                               taken for each object
    :param input_dir:    (str) path to directory containing the raw image files
    :param output_dir:   (str) path to directory that will contain processed
                               image files
    """
    # TODO: Add code below...
    # Should call the process_single_file function





