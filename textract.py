import boto3
import glob
import datetime
from gsheet import write_gsheet
import os
import pandas as pd


tim= datetime.datetime.now()

# Below code is check the extracted number from number plate and open the excel and write vehicle number and current time in " ENTRY SHEET " and delete the image in storage

def check_prev(result): # this function is used to check the detected number is new or previous
    with open('/home/admin1/yolov5/check.txt' ,'r') as filer:prev = filer.read()
    if result != prev:
        with open ('check.txt' ,'w') as filew:filew.write(result)
        return True
    
    else: return False  

def textextraction(input_file): # this function is used to extract the text

    temp_path = input_file
    imageBytes = bytearray(temp_path)
    
    # Amazon Textract client
    textract = boto3.client('textract')
    
    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})
    text = " "
    
    # Print detected text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text += item["Text"] + '\n'
    #print(text)
    return text


def aws():
    path = 'crop/'
    for image in glob.glob(path+'*.jpg'):
        print(image)
        with open(image,'rb')as doc: result = textextraction(doc.read())
        result = result.replace('*','').replace(' ','').replace('\n','')
        print(result)
        
        if result[:2].isalpha() and result[2:4].isnumeric()==True:
            if result[4:6].isalpha() ==True:
                if result[6:].isnumeric()==True :
                    check = check_prev(result)
                    if check :
                        # update in excel sheet 
                        data = pd.read_excel('database.xlsx')
                        updated = data.append(pd.DataFrame([[result ,tim.strftime('%H:%M')]],columns= ['VEHICLE NUMBER' , 'ENTRY TIME']))
                        updated.to_excel('database.xlsx', index = False)
                        #write_gsheet(result , tim.strftime('%H:%M') , excel_row)
                        print('result=' ,result)
                        os.remove(image)
                        return None
                    
                    else:
                        os.remove(image)
                        return None 
                    
            elif result[4:5].isalpha() and result[6:].isnumeric()== True:
                check = check_prev(result)
                if check :
                    print('result=' ,result)
                    data = pd.read_excel('database.xlsx')
                    data = data.append(pd.DataFrame([[result ,tim.strftime('%H:%M')]],columns= ['VEHICLE NUMBER' , 'ENTRY TIME']))
                    data.to_excel('database.xlsx', index = False)
                    #write_gsheet(result , tim.strftime('%H:%M') , excel_row )
                    os.remove(image)
                    return None
                
                else:
                    os.remove(image)
                    return None
        else:
            os.remove(image)
            return None
