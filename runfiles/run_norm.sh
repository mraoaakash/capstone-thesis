#! /bin/bash
#PBS -N COL_NORM
#PBS -o COL_NORM_out.log
#PBS -e COL_NORM_err.log
#PBS -l ncpus=5
#PBS -q gpu

eval "$(conda shell.bash hook)"
conda activate COL_NORM

BASEPATH=/home/aakash.rao_asp24

PATHFROMDIR=$BASEPATH/capstone-thesis/utils/normalization/pick_images.py

echo "Running normalization script"
echo $PATHFROMDIR

python $PATHFROMDIR
