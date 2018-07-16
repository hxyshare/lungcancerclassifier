config = {#'datapath':'/mnt/local/huaxinyu/stage2/stage2_subset/',

          'datapath':'/mnt/local/huaxinyu/luna16/test_set/',
          'preprocess_result_path':'../data/prep_test_set/',
          'outputfile':'prediction.csv',
          
         'detector_model':'net_detector',
         'detector_param':'./model/detector.ckpt',
         'classifier_model':'net_classifier',
         'classifier_param':'./model/classifier.ckpt',
         'n_gpu':1,
         'n_worker_preprocessing':12,
         'use_exsiting_preprocessing':False,
         'skip_preprocessing':True,
         'skip_detect':True}
