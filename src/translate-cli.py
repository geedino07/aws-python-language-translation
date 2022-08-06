import boto3
import click

@click.command()
@click.option('--phrase', prompt='Put in a phrase in any language to translate to english', 
    help='this is a tool that translates text to English language')

def action(phrase):
    client = boto3.client('translate', region_name="us-east-1")
    #text = "estoy enamorado de mi esposa"
    click.echo(click.style(f"Translate phrase: {phrase}", fg='red'))
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto",
        TargetLanguageCode="en")
    text = result['TranslatedText']
    click.echo(click.style(f'{text}', bg='blue', fg='white'))
#print (result)
#print(result['TranslatedText']) to filter and print only translated text

if __name__=='__main__':
    action()