export BERT_BASE_DIR=/home/xu/storage/work_tfg/chinese_Roberta_wwm
CUDA_VISIBLE_DEVICES=0,1 python3 run_pretraining.py --input_file=./tf_records_all/tf*.tfrecord  \
	--output_dir=/home/xu/storage/work_tfg/cmeie_roberta_wwm --use_tpu=False --do_train=True --do_eval=True --bert_config_file=$BERT_BASE_DIR/bert_config.json \
	--train_batch_size=256 --max_seq_length=256 --max_predictions_per_seq=23 \
	--num_train_steps=200000 --num_warmup_steps=10000 --learning_rate=1e-4    \
	--save_checkpoints_steps=3000  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt  &
