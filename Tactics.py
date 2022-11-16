import pandas as pd
import requests
from lxml import etree
import json
def getMapping():
    Te2Tamapping={}
    Ta2Temapping={}
    page=requests.get(url='https://attack.mitre.org/')
    page=etree.HTML(page.text)
    tactics=page.xpath("//*[@class='tactic name']/a/text()")
    technique_tds=page.xpath("//td[@class='tactic']")
    for index,td in enumerate(technique_tds):
        tactic=tactics[index].strip().lower()
        techniques=td.xpath(".//td[@class='technique']/div/a/text()")
        techniques=[technique.strip().lower() for technique in techniques]
        Ta2Temapping[tactic]=techniques
        for technique in techniques:
            Te2Tamapping[technique]=tactic


    with open('data/Te2TaMapping.json', 'w') as fp:
        json.dump(Te2Tamapping, fp)
    with open('data/Ta2TeMapping.json', 'w') as fp:
        json.dump(Ta2Temapping, fp)
def mapIntoTactics():
    with open('data/Te2TaMapping.json', 'r') as fp:
        mapping=json.load(fp)

    df = pd.read_csv('data/labeled.csv')
    df['tactic']=df['Technique'].apply(lambda x: mapping.get(x))
    df.to_csv('data/labeled_TacticMapped.csv')
if __name__=='__main__':
    getMapping()
    mapIntoTactics()