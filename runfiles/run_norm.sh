#! /bin/bash
#PBS -N COL_NORM
#PBS -o COL_NORM.log
#PBS -e COL_NORM.log
#PBS -l ncpus=5
#PBS -q cpu

eval "$(conda shell.bash hook)"
conda activate COL_NORM

BASEPATH=/home/aakash.rao_asp24

PATHFROMDIR={$BASEPATH}/utils/normalization/pick_images.py

echo "Running normalization script"
echo "{$PATHFROMDIR}"
