class AppExceptionCase(Exception):
    
    def __init__(self, status_code: int, context: dict):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.context = context
    
    def __str__(self):
        return (f"<AppException {self.exception_case} - "+ f"status_code={self.status_code} - context={self.context}>")
        
class AppException:
    
    class CreateLibro(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo creacion de libro
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
    
    class ReadLibros(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo lectura de libros
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
        
    class ReadLibro(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo lectura de libro
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
            
    class DeleteLibro(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo al eliminar el libro
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)
#######################################################################################

    class CreateAutor(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo creacion de autor
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)

    class ReadAutor(AppExceptionCase):
        
        def __init__(self, context: dict = None):
            """
            Fallo lectura de autor
            """
            status_code = 500
            AppExceptionCase.__init__(self, status_code, context)