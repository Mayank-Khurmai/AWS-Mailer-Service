import boto3

def send_mail(error_code, subject, message):
    client = boto3.client('sns')
    snsArn = 'arn:aws:sns:ap-south-1:660061364911:api-400-error'
 
    response = client.publish(
        TopicArn=snsArn,
        Message=message ,
        Subject='Eror in API',
        MessageStructure='html'
    )

    return response
