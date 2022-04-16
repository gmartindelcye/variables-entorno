Ejemplo de uso de las librerías python-dotenv y python-decouple
===============================================================

**decouple** automáticamente busca un archivo .env a nivel del proyecto donde se colocan las variables del proyecto.


Si se corre este proyecto, la impresión dará para la variable *"USER"* un valor diferente al 
del definido en el archivo porque USER es también una variable de entorno del sistema y toma
precendencia el entorno de el archvo .env. Este comportamiento en útil o no dependiendo si se usan variables de entorno y en su caso hay que tener en cuenta cuando se usan las misma en el archivo de configuración.

Normalmente se entrega un archivo file::.env-example para ser renombrado a file::.env para solo 
cambiar los valores necesarios en la aplicación particular 