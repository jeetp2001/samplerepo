import xlsxwriter
import psycopg2

con = psycopg2.connect(host='localhost',user='postgres',password='jeetp2001',database='gst')
cur = con.cursor()

workbook = xlsxwriter.Workbook('GSTR Filing Data - 092021.xlsx')

q1='select * from txnvalidations'
cur.execute(q1)
d1=cur.fetchall()

q2='select * from gst1hsn'
cur.execute(q2)
d2=cur.fetchall()

q3='select * from gstr1b2c'
cur.execute(q3)
d3=cur.fetchall()

q4='select * from gstr3b'   
cur.execute(q4)
d4=cur.fetchall()
 
q5='select * from mastererrorview order by errorlevel'
cur.execute(q5)
d5 = cur.fetchall()

ws5 = workbook.add_worksheet('Summary')
ws1 = workbook.add_worksheet('Transaction Errors')
ws2 = workbook.add_worksheet('GSTR-1HSN')
ws3 = workbook.add_worksheet('GSTR-1B2C')
ws4 = workbook.add_worksheet('GSTR-3B')

bold = workbook.add_format({'bold': True})

r1=c1=r2=c2=r3=c3=r4=c4=r5=c5=0

ws5.write(r5,c5,'Error Level',bold)
ws5.write(r5,c5+1,'Error Reason',bold)
ws5.write(r5,c5+2,'Error Type',bold)
ws5.write(r5,c5+3,'Column Name',bold)
ws5.write(r5,c5+4,'Number Of Instances',bold)

ws1.write(r1,c1,'CSV Row Number',bold)
ws1.write(r1,c1+1,'Invoice Number',bold)
ws1.write(r1,c1+2,'Booth Name And Number',bold)
ws1.write(r1,c1+3,'Error Message',bold)
ws1.write(r1,c1+4,'Error Name',bold)
ws1.write(r1,c1+5,'Period',bold)
ws1.write(r1,c1+6,'Customer GSTIN',bold)
ws1.write(r1,c1+7,'Error Level',bold)

ws2.write(r2,c2,'Return Period',bold)
ws2.write(r2,c2+1,'HSN',bold)
ws2.write(r2,c2+2,'GSTIN',bold)
ws2.write(r2,c2+3,'Unit Of Measurement',bold)
ws2.write(r2,c2+4,'GST',bold)
ws2.write(r2,c2+5,'Quantity',bold)
ws2.write(r2,c2+6,'Total',bold)
ws2.write(r2,c2+7,'Taxable Value',bold)
ws2.write(r2,c2+8,'CGST',bold)
ws2.write(r2,c2+9,'SGST',bold)

ws3.write(r3,c3,'Return Period',bold)
ws3.write(r3,c3+1,'GSTIN',bold)
ws3.write(r3,c3+2,'GST',bold)
ws3.write(r3,c3+3,'Quantity',bold)
ws3.write(r3,c3+4,'Total',bold)
ws3.write(r3,c3+5,'Taxable Value',bold)
ws3.write(r3,c3+6,'CGST',bold)
ws3.write(r3,c3+7,'SGST',bold)

ws4.write(r4,c4,'Return Period',bold)
ws4.write(r4,c4+1,'GSTIN',bold)
ws4.write(r4,c4+2,'Total Sale Invoice Value',bold)
ws4.write(r4,c4+3,'Taxable Sale Value',bold)
ws4.write(r4,c4+4,'Sale CGST',bold)
ws4.write(r4,c4+5,'Sale SGST',bold)
ws4.write(r4,c4+6,'Exempt Sale Invoice Value',bold)
ws4.write(r4,c4+7,'Exempt Purchase Value Intra',bold)
ws4.write(r4,c4+8,'Exempt Purchase Value Inter',bold)
ws4.write(r4,c4+9,'Taxable Purchase Value',bold)
ws4.write(r4,c4+10,'Pur Integrated Tax Amount',bold)
ws4.write(r4,c4+11,'Pur Central Tax Amount',bold)
ws4.write(r4,c4+12,'Pur StateUT Tax Amount',bold)
ws4.write(r4,c4+13,'Pur Cess Amount Advalorem',bold)
ws4.write(r4,c4+14,'Pur Cess Amount Specific',bold)
ws4.write(r4,c4+15,'CGST Payable',bold)
ws4.write(r4,c4+16,'SGST Payable',bold)

for i in d5:
    ws5.write(r5+1,c5,i[0])
    ws5.write(r5+1,c5+1,i[1])
    ws5.write(r5+1,c5+2,i[2])
    ws5.write(r5+1,c5+3,i[3])
    ws5.write(r5+1,c5+4,i[4])
    r5+=1

for i in d1:
    ws1.write(r1+1,c1,i[0])
    ws1.write(r1+1,c1+1,i[1])
    ws1.write(r1+1,c1+2,i[2])
    ws1.write(r1+1,c1+3,i[3])
    ws1.write(r1+1,c1+4,i[4])
    ws1.write(r1+1,c1+5,i[5])
    ws1.write(r1+1,c1+6,i[6])
    ws1.write(r1+1,c1+7,i[7])
    r1+=1

for i in d2:
    ws2.write(r2+1,c2,i[0])
    ws2.write(r2+1,c2+1,i[1])
    ws2.write(r2+1,c2+2,i[2])
    ws2.write(r2+1,c2+3,i[3])
    ws2.write(r2+1,c2+4,i[4])
    ws2.write(r2+1,c2+5,i[5])
    ws2.write(r2+1,c2+6,i[6])
    ws2.write(r2+1,c2+7,i[7])
    ws2.write(r2+1,c2+8,i[8])
    ws2.write(r2+1,c2+9,i[9])
    r2+=1
    
for i in d3:
    ws3.write(r3+1,c3,i[0])
    ws3.write(r3+1,c3+1,i[1])
    ws3.write(r3+1,c3+2,i[2])
    ws3.write(r3+1,c3+3,i[3])
    ws3.write(r3+1,c3+4,i[4])
    ws3.write(r3+1,c3+5,i[5])
    ws3.write(r3+1,c3+6,i[6])
    ws3.write(r3+1,c3+7,i[7])
    r3+=1

for i in d4:
    ws4.write(r4+1,c4,i[0])
    ws4.write(r4+1,c4+1,i[1])
    ws4.write(r4+1,c4+2,i[2])
    ws4.write(r4+1,c4+3,i[3])
    ws4.write(r4+1,c4+4,i[4])
    ws4.write(r4+1,c4+5,i[5])
    ws4.write(r4+1,c4+6,i[6])
    ws4.write(r4+1,c4+7,i[7])
    ws4.write(r4+1,c4+8,i[8])
    ws4.write(r4+1,c4+9,i[9])
    ws4.write(r4+1,c4+10,i[10])
    ws4.write(r4+1,c4+11,i[11])
    ws4.write(r4+1,c4+12,i[12])
    ws4.write(r4+1,c4+13,i[13])
    ws4.write(r4+1,c4+14,i[14])
    ws4.write(r4+1,c4+15,i[15])
    ws4.write(r4+1,c4+16,i[16])
    r4+=1
    
con.commit()
workbook.close()
print('done!')