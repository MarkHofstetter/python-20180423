import sort_image
import os, shutil

def test_flatten_dir():
    
    test_target_dir = os.path.join('test', 'result')
    try:
        shutil.rmtree(test_target_dir)
    except FileNotFoundError:
        pass
    
    sort_image.flatten_dir(os.path.join('test', 'data'),
                           test_target_dir)
    
    test_files = [
        'data_a_b_c_katze_auf_Mauer.jfif',
        'data_a_katzenhasen.jfif',
        'data_g_4asdf_asd.jfif'
    ]
    
    for i, filename in enumerate(os.listdir(test_target_dir)):
        assert filename in test_files
    
    assert i == len(test_files) - 1
    
                            