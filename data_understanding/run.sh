BASE=/Users/mraoaakash/Documents/research/Capstone_Thesis/capstone-thesis
EPOCHS=100
BATCH_SIZE=200


# python3 extract_nuclei.py \
#     -i $BASE/data/master/EvaluationSet/rgb\
#     -m $BASE/data/master/EvaluationSet/csv\
#     -s $BASE/data/individual_nuclei

python3 summarise_nuclei.py \
    -i $BASE/data/individual_nuclei\
    -o $BASE/data/individual_nuclei/summary