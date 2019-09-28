import boto3

def detect_labels_local_file(photo):


    client=boto3.client('rekognition',region_name='us-east-1')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        return(response['Labels'][0]['Name'])
    '''   
    #print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
    '''
def main():
    photo='2bottles.jpg'

    label_count=detect_labels_local_file(photo)
    #print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()