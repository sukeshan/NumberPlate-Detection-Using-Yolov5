# NumberPlate-Detection-Using-Yolov5


dataset with annotation : https://drive.google.com/drive/folders/1sW_1-s0E8sX4ZBs8x_HGZkk12AJDnVop?usp=sharing

weight :  https://drive.google.com/file/d/10R8BKgnfCAmylta9-iWSi_eiXFIo1JKW/view?usp=sharing

 **FLOW:**
   
   Using yolo version5 detect the numberplate and send it to AWS Textract and store it on excel sheet or googlesheet.
   
 **Things To do**

First thing all you know is install the prereqiurements.
 
    pip instal -r requirements.txt

Second is simple than you thinking run the detect.py script on your terminal

In this project, I used yolo medium size model the pretrained weight link mention in above .It's memory size comes around approximately 44mb .Then use detect.py script run the model. i added the few function in detect.py if you dont want remove that in detect.py
          
    python path/detect.py --weights path/weight.pt --source (image or video path or use 0 for webcam) --svae-crop(after detection pass it to aws  and store number in excel if you pass this arguments)
