import os
import boto3
import mimetypes

def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='AKIAZR3IWTCZWC4AV645',
        aws_secret_access_key='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',
        region_name='ap-northeast-2',
    )
    ''
    s3 = session.resource('s3')
    bucket = s3.Bucket('portfolio.actingprogrammer.io')

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            mime_type = mimetypes.guess_type(full_path)
            with open(full_path, 'rb') as data:
                if mime_type[0]:
                    bucket.put_object(Key=""+(full_path.replace("\\","/"))[len(path) + 1:],
                                      Body=data, ACL='public-read', ContentType=mime_type[0])
                else:
                    bucket.put_object(Key="" (full_path.replace("\\","/"))[len(path) + 1:],
                                      Bdoy=data, ACL='public-read')