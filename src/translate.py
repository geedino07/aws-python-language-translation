import boto3

client = boto3.client('translate', region_name="us-east-1")
text = "estoy enamorado de mi esposa"
result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")
print (result)
#print(result['TranslatedText']) to filter and print only translated text