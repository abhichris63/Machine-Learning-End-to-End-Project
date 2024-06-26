import os
import sys

# By obtaining(Deriving) Exception parent class we are creating our own HousingException class.
class HousingException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):

        # Super() means Parent class : To Parent Class Initializer i am passing error message.
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                         error_detail=error_detail)


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:

        """
        error_message: Exception object
        error_detail: object of sys module
        """

        _,_,exec_tb = error_detail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""

        Error occured in Script: 
        [ {file_name} ] at  
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] \
        error message: [{error_message}]
        
        """

        return error_message
    
    # Dunder Method
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()


