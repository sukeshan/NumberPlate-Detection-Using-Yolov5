# NumberPlate Detection Using Yolo Version 5



https://user-images.githubusercontent.com/48553042/143177283-f274dc3e-2f80-49f0-80d4-78707dca53dc.mp4



Annotated Dataset : https://drive.google.com/drive/folders/1sW_1-s0E8sX4ZBs8x_HGZkk12AJDnVop?usp=sharing

The Annotated Dataset contain 931 data points (Indian Car with variable image size)

Pretrained weight file :  https://drive.google.com/file/d/10R8BKgnfCAmylta9-iWSi_eiXFIo1JKW/view?usp=sharing

 # FLOW
   
   Using yolo version5 detect the numberplate and send it to AWS Textract and store it on excel sheet or googlesheet.
   
# Description

   I used yolo version 5 medium size model for training so if you want to fine tune the pretrained model by using your own datasets then you can only use medium size architecture and also image size should be 640*640 . 

# Detect Number Plate
**Instal requirements**

    pip instal -r requirements.txt
    

**Detection**

    python detect.py --weights (weight path) --source (image or video path or use 0 for webcam) --svae-crop(after detection pass it to aws  and store number in excel if you pass this arguments) --save-txt (save results to *.txt)
  
**Fine Tune**

Before you fine tune the pretrained model you should mention the data path on datapath.yaml file 

    python train.py --img 640 --batch (depends on your GPU) --epoch (your wish) --data data/datapath --weight (pretrained weight) --cfg models/yolov5m.yaml 

 
