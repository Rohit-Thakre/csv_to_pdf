import PyPDF2
import re
import csv

filename = "data.csv"
csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile) 



with open('demo.pdf' ,'rb') as pdf_obj:
    pdf = PyPDF2.PdfReader(pdf_obj)
    page_size = len(pdf.pages)

    for no in range(page_size): 
        page_obj = pdf.pages[no]
        # start_from 120
        page_text = page_obj.extract_text()[120:]
       
        page_list = re.split(r'OMR\n', page_text)
        # last me ORM add karn hai, since ORM\n se splite kr rahe hai to vo remove kiya hai 


        for line in page_list:
            try:
                posting_date = re.findall(r'\d{2}\s\w{3}\s\d{4}', line)[0]
                value_date = re.findall(r'\d{2}\s\w{3}\s\d{4}', line)[1]




                line = line+'OMR'
                amt = re.findall(r'\-*\d{1,3}\.\d{1,}\sOMR', line)
                amount = amt[0]
                ac_bal = amt[1]


                
                des = line[23: ]
                description = re.sub(r"\-*\d{1,3}\.\d{1,}\sOMR", " ", des)
                
                row = [posting_date.strip() , value_date.strip(), description.strip(), amount.strip(), ac_bal.strip(),]
                
                csvwriter.writerow(row) 

                
            except:
                pass


csvfile.close()
print('data saved.')

        
        
            

