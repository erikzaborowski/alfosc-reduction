#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors:
#   - Erik Zaborowski
#   - Finian Ashmead
#   - Isaac Sierra
#   - Mike Gladders

import os
import sys
import numpy as np
import argparse
import pandas as pd
import time
import datetime
import timeit
from astropy.io import fits
from astropy.table import Table


def process_single_file(input_file):
    """
    Function to take a FITS image and subtract the mean value of the
    overscan area of the CCD.
    :param input_file:    (str) filepath of the image to process
    :returns output_hdul: (astropy.io.fits.HDUList) processed version of the fits file
    """
    hdul = fits.open(input_file)
    data = hdul[1].data
    hdr = hdul[1].header
    vals = data[:,2120:2140]
    avg_pix = np.mean(vals)
    subtracted_data = data - avg_pix
    #hdu_primary = fits.PrimaryHDU()
    #hdu_subtracted = fits.ImageHDU(subtracted_data, header=hdr)
    #output_hdul = fits.HDUList([hdu_primary, hdu_subtracted])
    hdu_subtracted = fits.PrimaryHDU(subtracted_data, header=hdr)
    output_hdul = fits.HDUList([hdu_subtracted])
    return output_hdul

def process_all_objects(filepath_ctrlfile, input_dir, output_dir):
    """
    Function to loop through the files in the input directory and process them/save
    them in an output directory.
    
    Control file should be in the format (one object per line):
        object_name1 science1 science2 flat1 flat2 arc1 arc2
        object_name2 science1 science2 flat1 flat2 arc1 arc2
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
    df_ctrlfile = pd.read_csv(filepath_ctrlfile)
    print('Control file')
    print(df_ctrlfile)
    for i in np.arange(len(df_ctrlfile)):
        # Load sci1, sci2, flat1, flat2 from control file
        object_name = df_ctrlfile.loc[i, 'object']
        filepath_sci1 = os.path.join(input_dir, df_ctrlfile.loc[i, 'sci1'])
        filepath_sci2 = os.path.join(input_dir, df_ctrlfile.loc[i, 'sci2'])
        filepath_flat1 = os.path.join(input_dir, df_ctrlfile.loc[i, 'flat1'])
        filepath_flat2 = os.path.join(input_dir, df_ctrlfile.loc[i, 'flat2'])

        # Run processing on each of these
        sci1_processed = process_single_file(filepath_sci1)
        sci2_processed = process_single_file(filepath_sci2)
        flat1_processed = process_single_file(filepath_flat1)
        flat2_processed = process_single_file(filepath_flat2)

        # Save outputs in renamed files in IRAF directory "testnest"
        parentdir = os.path.dirname(os.path.abspath(__file__))
        sci1_processed.writeto(os.path.join(parentdir, 'sci1.fits'), overwrite=True)
        sci2_processed.writeto(os.path.join(parentdir, 'sci2.fits'), overwrite=True)
        flat1_processed.writeto(os.path.join(parentdir, 'flat1.fits'), overwrite=True)
        flat2_processed.writeto(os.path.join(parentdir, 'flat2.fits'), overwrite=True)

        # Call IRAF processing
        iraf_path = os.path.join(parentdir, 'irafskysub')
        cmd = f'cl < {iraf_path}'
        print(cmd)
        os.system(cmd)

        # Rename outputs and move to output directory
        os.rename(os.path.join(parentdir, 'diffsubfinal.fits'), os.path.join(output_dir, object_name + '_diffsubfinal.fits'))
        os.rename(os.path.join(parentdir, 'skysubfinal.fits'), os.path.join(output_dir, object_name + '_skysubfinal.fits'))

if __name__ == '__main__':
    description = 'Pipeline to run a single night of ALFOSC data and produce 2-D sky-subtracted images'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-c', '--control-file', type=str, dest='ctrlfile', help="Path to control file which specifies the data taken that night")
    parser.add_argument('-i', '--indir', type=str, dest='indir', help="Path to input directory containing raw images")
    parser.add_argument('-o', '--outdir', type=str, dest='outdir', help="Path to output directory to contain sky-subtracted images")
    args = parser.parse_args()

    process_all_objects(filepath_ctrlfile=args.ctrlfile, input_dir=args.indir, output_dir=args.outdir)

