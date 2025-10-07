import re
def openFile(filepath):
    typeLim = None
    typePrimitive = None
    with open(filepath,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if  line.startswith('@'):
                parts = line.split(',')
                typeLim = parts[0]
                typeLim= typeLim.replace('@','').replace('(','')  
                if typeLim.startswith('Patternregexp'):
                        typeLim = typeLim.replace('Patternregexp = "', '')
                        typeLim = '"(' + typeLim
                        typeLim = re.sub(r'^.*?\)', '', typeLim)
                        colchetes = re.findall(r'\[([^\]]+)\]', typeLim)
                        if colchetes:
                            typeLim = list(colchetes[0])
                        elif ')' in typeLim:
                            typeLim =  typeLim.replace('$','').replace('"','').replace(')','')
                            typeLim = [v.strip() for v in typeLim.split('|') if v.strip()] 
            if line.startswith('private'):
                partype = line.split()
                print(f'Campo do comentario: {partype[2]}')
                print("----------------------------")
                typePrimitive = partype[1]
            """ if 'NotBlankmessage' in typeLim:
                print('Necessario uma requisição') """
            if typeLim:
                print(f'// Tipo:{typePrimitive} e seu valor: {typeLim}')
                typeLim = None

openFile(r'D:\Hera\src\main\java\com\vockan\erp\standard\core\dto\CurrencyDTO.java')