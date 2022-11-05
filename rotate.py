from flask import request
from flask_restful import Resource
from PyPDF2 import PdfFileReader, PdfFileWriter


class RotatePdf(Resource):
    def post(self):
        input_data = request.get_json()
        target_file = input_data['file_path']

        output_path = 'rotated.pdf' 

        output_file = open(output_path, 'wb')
        pdf = PdfFileReader(target_file)
        writer = PdfFileWriter()

        # total number of pages
        pages = pdf.getNumPages()

        # the page number to rotate
        page_number = int(input_data['page_number']) - 1

        # angle of rotation
        angle_of_rotation = int(input_data['angle_of_rotation'])



        for i in range(pages):
            if (i == page_number):
                rotation = angle_of_rotation
            else:
                rotation = 0 
            page = pdf.getPage(i)
            page.rotateClockwise(rotation)
            writer.addPage(page)
        
        writer.write(output_file)
        output_file.close()

        return {'Output Path': output_path}, 201