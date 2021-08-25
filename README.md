# NumberPlate-Detection-Using-Yolov5


Dataset with annotation : https://drive.google.com/drive/folders/1sW_1-s0E8sX4ZBs8x_HGZkk12AJDnVop?usp=sharing

Pretrained weight :  https://drive.google.com/file/d/10R8BKgnfCAmylta9-iWSi_eiXFIo1JKW/view?usp=sharing

 **FLOW:**
   
   Using yolo version5 detect the numberplate and send it to AWS Textract and store it on excel sheet or googlesheet.
   
 **Getting started:**

First thing all you know is install the prereqiurements.
 
    pip instal -r requirements.txt

Second is simple than you thinking run the detect.py script on your terminal and I mentioned the pretrained weight in above link.
          
    python path/detect.py --weights path/weight.pt --source (image or video path or use 0 for webcam) --svae-crop(after detection pass it to aws  and store number in excel if you pass this arguments)
   
   
Let's talk about the dataset because 50% of work in Machine Learning is data preparation and preprocessing . In this model I used only real life data and I prepared 931 datapoints (I mentioned the dataset with annotation in above link) . For reducing the noise I cropped the background images and I didn't do the data augmentation for this model . I used an 8: 2 ratio when splitting data for training and validation . For testing model I used data which I downloaded from kaggle . Coming to the model I used Yolo Version 5 medium size model  . I think it is very cool because I used the same dataset and put data in the training on yolo version 3 and version 5 .I used the Tesla P100 Gpu for training for both a model . Yolov3 took 90 minutes(approx) for me to complete 100 epochs and it's weight is 245 mb(approx) but yolov5 took only 45 minutes(approx) and it's weight is 44mb (approx) and also it is very good in accuracy too .
