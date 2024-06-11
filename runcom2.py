import os
import natsort as nt

path = os.path.join(os.getcwd(), 'data/content-images/content_0to59')
path_style = os.path.join(os.getcwd(), 'data/my_style/spring')

img_list = nt.natsorted(os.listdir(path))
style_list = nt.natsorted(os.listdir(path_style)) 


for i, img in enumerate(img_list): # 30

    os.system(f'python neural_style_transfer.py --content_img_name content_0to59/{img} --style_img_name spring/spring3.jpg --output_dir_name output-images/spring3')
#################################봄!!!##################################################
path = os.path.join(os.getcwd(), 'data/content-images/content_60to119')
path_style = os.path.join(os.getcwd(), 'data/my_style/summer')

img_list = nt.natsorted(os.listdir(path))
style_list = nt.natsorted(os.listdir(path_style))


for i, img in enumerate(img_list): # 30

    os.system(f'python neural_style_transfer.py --content_img_name content_60to119/{img} --style_img_name summer/summer4.jpg --output_dir_name output-images/summer4')

#####################################여름!!####################################################
path = os.path.join(os.getcwd(), 'data/content-images/content_120to179')
path_style = os.path.join(os.getcwd(), 'data/my_style/autumn')

img_list = nt.natsorted(os.listdir(path))
style_list = nt.natsorted(os.listdir(path_style))


for i, img in enumerate(img_list): # 30

    os.system(f'python neural_style_transfer.py --content_img_name content_120to179/{img} --style_img_name autumn/autumn2.jpg --output_dir_name output-images/autumn2')

#####################################가을!!####################################################
path = os.path.join(os.getcwd(), 'data/content-images/content_180to239')
path_style = os.path.join(os.getcwd(), 'data/my_style/winter')

img_list = nt.natsorted(os.listdir(path))
style_list = nt.natsorted(os.listdir(path_style))


for i, img in enumerate(img_list): # 30

    os.system(f'python neural_style_transfer.py --content_img_name content_180to239/{img} --style_img_name winter/winter4.jpg --output_dir_name output-images/winter4')
########################################겨울!!#################################################
