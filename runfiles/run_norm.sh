#! /bin/bash
#PBS -N COL_NORM
#PBS -o COL_NORM_out.log
#PBS -e COL_NORM_err.log
#PBS -l ncpus=5
#PBS -q gpu

module load compiler/anaconda3


eval "$(conda shell.bash hook)" 
conda activate COL_NORM


echo "Running normalization script"

python /home/aakash.rao_asp24/capstone-thesis/utils/normalization/pick_images.py \
    --input_dir /home/aakash.rao_asp24/capstone-thesis/data/NuclsEvalSet/rgb \
    --output_dir /home/aakash.rao_asp24/capstone-thesis/data/norm_images/ \
    --n 5 \
    --i 5 \
    --seed 42 \