
from . import basic_config

def infer_sent_v1():
    """
    set configs
    """
    config = basic_config.config()
    config.learning_rate = 0.1
    config.lr_decay = 0.99
    config.optimizer_type = 'sgd'
    config.save_dirname = "model_dir"
    config.use_pretrained_word_embedding = True
    config.dict_dim = 40000 # approx_vocab_size
    config.class_dim = 2

    # net config
    config.emb_dim = 300 
    config.droprate_lstm = 0.0
    config.droprate_fc = 0.0
    config.word_embedding_trainable = False
    config.rnn_hid_dim = 2048
    config.mlp_non_linear = False

    return config

def infer_sent_v2():
    """
    use our own config
    """
    config = basic_config.config()
    config.learning_rate = 0.0002
    config.lr_decay = 0.99
    config.optimizer_type = 'adam'
    config.save_dirname = "model_dir"
    config.use_pretrained_word_embedding = True
    config.dict_dim = 40000 # approx_vocab_size
    config.class_dim = 2

    # net config
    config.emb_dim = 300
    config.droprate_lstm = 0.0
    config.droprate_fc = 0.2
    config.word_embedding_trainable = False
    config.rnn_hid_dim = 2048
    config.mlp_non_linear = True

    return config
