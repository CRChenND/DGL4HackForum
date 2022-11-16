import pandas as pd

def readS():
   df=pd.read_csv('data/ransomare_family_victims_methods - HF-Shang.csv')
   df['Technique']=df['TECHNIQUE']
   df=df.iloc[df['Technique'].dropna().index, :]
   df['Technique']=df['Technique'].apply(lambda x: x.strip().lower())
   print(df['Technique'].value_counts())
   return df

def readC():
   df=pd.read_csv('data/ransomare_family_victims_methods - HF-Chaoran.csv')

   df=df.iloc[df['Technique'].dropna().index, :]
   df['Technique']=df['Technique'].apply(lambda x: x.strip().lower())
   return  df
def readA():
   df=pd.read_csv('data/ransomare_family_victims_methods - HF-Aditya.csv')
   df=df.iloc[df['Technique'].dropna().index, :]
   df['Technique']=df['Technique'].apply(lambda x: x.strip().lower())
   return df

def mergeDF():
   df=pd.concat([readS(),readC(),readA()],axis=0)
   df.to_csv('data/labeled.csv',index=False)
   print(df['Technique'].value_counts())

def readMergedDF():
   df=pd.read_csv('data/labeled.csv')
   return df
if __name__=='__main__':
   # mergeDF()
   df=readMergedDF()
   # df= pd.read_csv('data/C')
   # df['thread_id']=df.thread_id.apply(lambda x: x.split('tid=')[-1])
   # nodes==df['thread_id'].unique()
   # nodes.extend(df['user_names'].unique())
   # edges