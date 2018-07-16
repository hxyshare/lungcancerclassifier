config = {'stage1_data_path':'/home/huaxinyu/project/lungcancer/data/stage1',
          'luna_raw':'/home/huaxinyu/project/lungcancer/data/luna_raw',
          'luna_segment':'/home/huaxinyu/project/lungcancer/data/luna/seg-lungs-LUNA16/',
          
          'luna_data':'/home/huaxinyu/project/lungcancer/data/luna/allset',
          'preprocess_result_path':'/home/huaxinyu/project/lungcancer/data/preprocess/',       
          'preprocess_result_subset':'/home/huaxinyu/project/lungcancer/data/preprocess_subset', 
          'luna_abbr':'./detector/labels/shorter.csv',
          'luna_label':'./detector/labels/lunaqualified.csv',
          'stage1_annos_path':['./detector/labels/label_job5.csv',
                './detector/labels/label_job4_2.csv',
                './detector/labels/label_job4_1.csv',
                './detector/labels/label_job0.csv',
                './detector/labels/label_qualified.csv'],
          'bbox_path':'../detector/results/res18/bbox/',
          'preprocessing_backend':'python'
         }
