import shutil

def iterarCopia(numero):
    for idLote in range(1,numero):
        for idDocumento in range(1,23):
            if idDocumento >= 1 and idDocumento <= 9:
                pathOrigen = 'C:\\Users\\sebas\\OneDrive\\Documentos\\Batch\\Recursos\\'+'0'+str(idDocumento)+'.pdf'
                pathDestino = 'C:\\Users\\sebas\\OneDrive\\Documentos\\Batch\\Destino\\'+'0'+str(idDocumento)+'-'+str(idLote)+'.pdf'
            else:
                pathOrigen = 'C:\\Users\\sebas\\OneDrive\\Documentos\\Batch\\Recursos\\'+ str(idDocumento)+'.pdf'    
                pathDestino = 'C:\\Users\\sebas\\OneDrive\\Documentos\\Batch\\Destino\\'+ str(idDocumento)+'-'+str(idLote)+'.pdf'
            try:
                shutil.copy(pathOrigen, pathDestino)
                print("File copied successfully.")
            
                # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
                
                # If there is any permission issue
            except PermissionError:
                print("Permission denied.")
                
                # For other errors
            except:
                print("Error occurred while copying file.")

iterarCopia(129)