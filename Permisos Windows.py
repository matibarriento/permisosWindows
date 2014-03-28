# -*- encoding: utf-8 -*-
import os
import platform as plat

def Version():
    win = plat.platform()
    version = []
    version = win.split('-')
    # print "Vesion ", version[1]
    return version[1]

root = os.getcwd()
usuarios = []
usuario = os.environ.get("USERNAME")
procesados=[]
totales = 0
vueltas = 0
accion = "G - Garantizar, R - Reemplazar, D - Denegar"
acceso = "R - Leer , W - Escribir, C - Cambiar (Leer/Escribir), F - Control Total, N - Ninguno"

# for path, subdirs, files in os.walk(root):
#    for name in files:
#       archivo = '"'+ os.path.join(path, name)+'"'
#       cmd  = "cacls "+ archivo
#       usuarios.append(os.system(cmd))

# print usuarios
if (Version() == 'XP'):
  print "Ingrese el nombre usuario a quien quiere dar permisos:"
  print "Ejmeplo: ",usuario,", NETWORK, otro"

  usuario = raw_input()

  os.system('cls')
  resp = True

  while resp:
     print "Ingrese el tipo de acción que desea realizar: "
     print accion
     acc = raw_input().lower()
     if (acc in ("g","r","d")):
        resp = False
     else:
        os.system('cls')
        print "Respuesta incorrecta"

  os.system('cls')
  resp = True

  while  resp:
     print "Ingrese el tipo de acceso que desea realizar: "
     print acceso
     accs = raw_input().upper()
     if (accs in ("R","W","C", "F","N")):
        resp = False
     else:
        os.system('cls')
        print "Respuesta incorrecta"

  print "Permisos para ",usuario

  print "ASEGURESE QUE ESTE ARCHIVO ESTE EN LA CARPETA DONDE DESEA HABILITAR LOS PERMISOS"

  rta = raw_input("Desea continuar S/N?")

  if(rta in ('s','S')):
      print "Empezando"
      for path, subdirs, files in os.walk(root):
          for name in files:
              # print name
              totales+= 1
              archivo = '"'+ os.path.join(path, name)+'"'
              cmd = "echo s| cacls "+ archivo+ "/e /" + acc + " " + usuario + ":" + accs
              if(os.system(cmd) == 0):
                  procesados.append(name)
              if vueltas == 7:
                 os.system('cls')
                 vueltas = 0
              else:
                 vueltas += 1

      print "Usuario con permisos: ",usuario

      # print "Archivos procesados: "
      # for archivo in procesados:
      #     print archivo,',',
      # print
      print "-------------------------"
      print "Se procesaron ",len(procesados)," archivos de ", totales,"\n",
  else:
      print "No se realizo ninguna acción"

  raw_input("Pulse para finalizar")

else:
  print "Esta version solo es apta para Windows XP"
  raw_input("Pulse para finalizar")

def Revision():
    for path, subdirs, files in os.walk(root):
        for name in files:
            print name
            archivo = '"'+ os.path.join(path, name)+'"'
            if(Version()== '7'):
                cmd = "icacls " + archivo
            elif (Version() == 'XP'):
                cmd = "echo s| cacls "+ archivo
            os.system(cmd)


